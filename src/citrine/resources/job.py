from logging import getLogger
from typing import List, Optional, Set, Dict, Union
from uuid import UUID

from time import time, sleep

from citrine._serialization.properties import Set as PropertySet, String, Object
from citrine._rest.resource import Resource
from citrine._serialization import properties
from citrine._session import Session
from citrine.exceptions import PollingTimeoutError, JobFailureError

logger = getLogger(__name__)


class JobSubmissionResponse(Resource['AraJobStatus']):
    """[ALPHA] a response to a submit-job request for the job submission framework.

    This is returned as a successful response from the remote service.

    Parameters
    ----------
    job_id: UUID
        job id of the of a job submission request

    """

    job_id = properties.UUID("job_id")

    def __init__(self, job_id: UUID):
        self.job_id = job_id


class TaskNode(Resource['TaskNode']):
    """[ALPHA] individual task status.

    The TaskNode describes a component of an overall job.

    Parameters
    ----------
    id: str
        unique identification number for the job task.
    task_type: str
        the type of task running
    status: str
        the last reported status of this particular task.
        One of "Submitted", "Pending", "Running", "Success", or "Failure".
    dependencies: Set[str]
        all the tasks that this task is dependent on.
    failure_reason: Optional[str]
        if a task has failed, the failure reason will be in this parameter.

    """

    id = properties.String("id")
    task_type = properties.String("task_type")
    status = properties.String("status")
    dependencies = PropertySet(String(), "dependencies")
    failure_reason = properties.Optional(String(), "failure_reason")

    def __init__(
            self,
            id: str,
            task_type: str,
            status: str,
            dependencies: Set[str],
            failure_reason: Optional[str]
    ):
        self.id = id
        self.task_type = task_type
        self.status = status
        self.dependencies = dependencies
        self.failure_reason = failure_reason


class JobStatusResponse(Resource['JobStatusResponse']):
    """[ALPHA] a response to a job status check.

    The JobStatusResponse summarizes the status for the entire job.

    Parameters
    ----------
    job_type: str
        the type of job for this status report
    status: str
        the actual status of the job.
        One of "Running", "Success", or "Failure".
    tasks: List[TaskNode]
        all of the constituent task required to complete this job
    output: Optional[Map[String,String]]
        job output properties and results

    """

    job_type = properties.String("job_type")
    status = properties.String("status")
    tasks = properties.List(Object(TaskNode), "tasks")
    output = properties.Optional(properties.Mapping(String, String), 'output')

    def __init__(
            self,
            job_type: str,
            status: str,
            tasks: List[TaskNode],
            output: Optional[Dict[str, str]]
    ):
        self.job_type = job_type
        self.status = status
        self.tasks = tasks
        self.output = output


def _poll_for_job_completion(session: Session, project_id: Union[UUID, str],
                             job: Union[JobSubmissionResponse, UUID, str], *,
                             timeout: float = 2 * 60,
                             polling_delay: float = 2.0) -> JobStatusResponse:
    """
    Polls for job completion given a timeout, failing with an exception on job failure.

    This polls for job completion given the Job ID, failing appropriately if the job result
    was not successful.

    Parameters
    ----------
    job
        The job submission object or job ID that was given from a job submission.
    timeout
        Amount of time to wait on the job (in seconds) before giving up. Defaults
        to 2 minutes. Note that this number has no effect on the underlying job
        itself, which can also time out server-side.
    polling_delay:
        How long to delay between each polling retry attempt.

    Returns
    -------
    JobStatusResponse
        The job response information that can be used to extract relevant
        information from the completed job.

    """
    if isinstance(job, JobSubmissionResponse):
        job_id = job.job_id
    else:
        job_id = job  # pragma: no cover
    path = 'projects/{}/execution/job-status'.format(project_id)
    params = {'job_id': job_id}
    start_time = time()
    while True:
        response = session.get_resource(path=path, params=params)
        status: JobStatusResponse = JobStatusResponse.build(response)
        if status.status in ['Success', 'Failure']:
            break
        elif time() - start_time < timeout:
            logger.info('Job still in progress, polling status again in {:.2f} seconds.'
                        .format(polling_delay))

            sleep(polling_delay)
        else:
            logger.error('Job exceeded user timeout of {} seconds.'.format(timeout))
            logger.debug('Last status: {}'.format(status.dump()))
            raise PollingTimeoutError('Job {} timed out.'.format(job_id))
    if status.status == 'Failure':
        logger.debug('Job terminated with Failure status: {}'.format(status.dump()))
        failure_reasons = []
        for task in status.tasks:
            if task.status == 'Failure':
                logger.error('Task {} failed with reason "{}"'.format(
                    task.id, task.failure_reason))
                failure_reasons.append(task.failure_reason)
        raise JobFailureError(
            message='Job {} terminated with Failure status. Failure reasons: {}'.format(
                job_id, failure_reasons), job_id=job_id,
            failure_reasons=failure_reasons)

    return status