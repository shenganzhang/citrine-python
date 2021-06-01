"""Resources that represent both individual and collections of design workflow executions."""
from functools import partial
from typing import Optional, Iterable, Union
from uuid import UUID

from citrine._rest.collection import Collection
from citrine._rest.paginator import Paginator
from citrine._rest.pageable import Pageable
from citrine._rest.resource import Resource
from citrine._rest.asynchronous_object import AsynchronousObject
from citrine._serialization import properties
from citrine._session import Session
from citrine.informatics.design_candidate import DesignCandidate
from citrine.resources.response import Response
from citrine.informatics.scores import Score
from citrine.informatics.descriptors import Descriptor


class DesignExecution(Resource['DesignExecution'], Pageable, AsynchronousObject):
    """The execution of a DesignWorkflow.

    Possible statuses are INPROGRESS, SUCCEEDED, and FAILED.
    Design executions also have a ``status_description`` field with more information.

    """

    _paginator: Paginator = Paginator()
    _collection_key = 'response'
    _session: Optional[Session] = None
    project_id: Optional[UUID] = None
    """:Optional[UUID]: Unique ID of the project that contains this workflow execution."""

    uid: UUID = properties.UUID('id', serializable=False)
    """:UUID: Unique identifier of the workflow execution"""
    workflow_id = properties.UUID('workflow_id', serializable=False)
    """:UUID: Unique identifier of the workflow that was executed"""
    version_number = properties.Integer("version_number", serializable=False)
    """:int: Integer identifier that increases each time the workflow is executed. The first
    execution has version_number = 1."""

    status = properties.Optional(properties.String(), 'status', serializable=False)
    """:Optional[str]: short description of the execution's status"""
    status_description = properties.Optional(
        properties.String(), 'status_description', serializable=False)
    """:Optional[str]: more detailed description of the execution's status"""
    status_info = properties.Optional(
        properties.List(properties.String()),
        'status_info',
        serializable=False
    )
    """:Optional[List[str]]: human-readable explanations of the status"""
    experimental = properties.Boolean("experimental", serializable=False, default=True)
    """:bool: whether the execution is experimental (newer, less well-tested functionality)"""
    experimental_reasons = properties.Optional(
        properties.List(properties.String()),
        'experimental_reasons',
        serializable=False
    )
    """:Optional[List[str]]: human-readable reasons why the execution is experimental"""
    created_by = properties.Optional(properties.UUID, 'created_by', serializable=False)
    """:Optional[UUID]: id of the user who created the resource"""
    updated_by = properties.Optional(properties.UUID, 'updated_by', serializable=False)
    """:Optional[UUID]: id of the user who most recently updated the resource,
    if it has been updated"""
    create_time = properties.Optional(properties.Datetime, 'create_time', serializable=False)
    """:Optional[datetime]: date and time at which the resource was created"""
    update_time = properties.Optional(properties.Datetime, 'update_time', serializable=False)
    """:Optional[datetime]: date and time at which the resource was most recently updated,
    if it has been updated"""

    score = properties.Object(Score, 'score')
    """:Score: score by which this execution was evaluated"""
    descriptors = properties.List(properties.Object(Descriptor), 'descriptors')
    """:List[Descriptor]: all of the descriptors in the candidates generated by this execution"""

    def __init__(self):
        """Design executions are not directly instantiated by the user."""
        pass  # pragma: no cover

    def __str__(self):
        return '<DesignExecution {!r}>'.format(str(self.uid))

    def _path(self):
        return '/projects/{project_id}/design-workflows/{workflow_id}/executions/{execution_id}' \
            .format(project_id=self.project_id,
                    workflow_id=self.workflow_id,
                    execution_id=self.uid)

    def in_progress(self) -> bool:
        """Whether design execution is in progress. Does not query state."""
        return self.status == "INPROGRESS"

    def succeeded(self) -> bool:
        """Whether design execution has completed successfully. Does not query state."""
        return self.status == "SUCCEEDED"

    def failed(self) -> bool:
        """Whether design execution has completed unsuccessfully. Does not query state."""
        return self.status == "FAILED"

    @classmethod
    def _build_candidates(cls, subset_collection: Iterable[dict]) -> Iterable[DesignCandidate]:
        for candidate in subset_collection:
            yield DesignCandidate.build(candidate)

    def candidates(self,
                   page: Optional[int] = None,
                   per_page: int = 100,
                   ) -> Iterable[DesignCandidate]:
        """Fetch the Design Candidates for the particular execution, paginated."""
        path = self._path() + '/candidates'

        fetcher = partial(self._fetch_page, path=path, fetch_func=self._session.get_resource)

        return self._paginator.paginate(page_fetcher=fetcher,
                                        collection_builder=self._build_candidates,
                                        page=page,
                                        per_page=per_page)


class DesignExecutionCollection(Collection["DesignExecution"]):
    """A collection of DesignExecutions."""

    _path_template = '/projects/{project_id}/design-workflows/{workflow_id}/executions'  # noqa
    _individual_key = None
    _collection_key = 'response'
    _resource = DesignExecution

    def __init__(self, *,
                 project_id: UUID,
                 session: Session,
                 workflow_id: Optional[UUID] = None):
        self.project_id: UUID = project_id
        self.session: Session = session
        self.workflow_id: UUID = workflow_id

    def build(self, data: dict) -> DesignExecution:
        """Build an individual DesignWorkflowExecution."""
        execution = DesignExecution.build(data)
        execution._session = self.session
        execution.project_id = self.project_id
        return execution

    def trigger(self, execution_input: Score):
        """Trigger a Design Workflow execution given a score."""
        path = self._get_path()
        data = self.session.post_resource(path, {'score': execution_input.dump()})
        self._check_experimental(data)
        return self.build(data)

    def register(self, model: DesignExecution) -> DesignExecution:
        """Cannot register an execution."""
        raise NotImplementedError("Cannot register a DesignExecution.")

    def update(self, model: DesignExecution) -> DesignExecution:
        """Cannot update an execution."""
        raise NotImplementedError("Cannot update a DesignExecution.")

    def archive(self, execution_id: UUID):
        """Archive a Design Workflow execution.

        Parameters
        ----------
        execution_id: UUID
            Unique identifier of the execution to archive

        """
        raise NotImplementedError(
            "Design Executions cannot be archived")

    def restore(self, execution_id: UUID):
        """Restore an archived Design Workflow execution.

        Parameters
        ----------
        execution_id: UUID
            Unique identifier of the execution to restore

        """
        raise NotImplementedError(
            "Design Executions cannot be restored")

    def list(self,
             page: Optional[int] = None,
             per_page: int = 100,
             ) -> Iterable[DesignExecution]:
        """
        Paginate over the elements of the collection.

        Leaving page and per_page as default values will yield all elements in the
        collection, paginating over all available pages.

        Parameters
        ---------
        page: int, optional
            The "page" of results to list. Default is to read all pages and yield
            all results.  This option is deprecated.
        per_page: int, optional
            Max number of results to return per page. Default is 100.  This parameter
            is used when making requests to the backend service.  If the page parameter
            is specified it limits the maximum number of elements in the response.
        predictor_id: uuid, optional
            list executions that targeted the predictor with this id

        Returns
        -------
        Iterable[ResourceType]
            Resources in this collection.

        """
        return self._paginator.paginate(page_fetcher=self._fetch_page,
                                        collection_builder=self._build_collection_elements,
                                        page=page,
                                        per_page=per_page)

    def delete(self, uid: Union[UUID, str]) -> Response:
        """Design Workflow Executions cannot be deleted or archived."""
        raise NotImplementedError(
            "Design Executions cannot be deleted")
