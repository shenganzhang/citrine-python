import uuid

import pytest

from citrine.informatics.modules import ModuleRef
from citrine.informatics.predictor_evaluation_result import PredictorEvaluationResult
from citrine.resources.predictor_evaluation_execution import PredictorEvaluationExecutionCollection, \
    PredictorEvaluationExecution
from tests.utils.session import FakeSession, FakeCall


@pytest.fixture
def session() -> FakeSession:
    return FakeSession()


@pytest.fixture
def collection(session) -> PredictorEvaluationExecutionCollection:
    return PredictorEvaluationExecutionCollection(
        project_id=uuid.uuid4(),
        workflow_id=uuid.uuid4(),
        session=session,
    )


@pytest.fixture
def workflow_execution(collection: PredictorEvaluationExecutionCollection, predictor_evaluation_execution_dict) -> PredictorEvaluationExecution:
    return collection.build(predictor_evaluation_execution_dict)


def test_basic_methods(workflow_execution, collection):
    assert "PredictorEvaluationExecution" in str(workflow_execution)

    with pytest.raises(TypeError):
        workflow_execution[12]

    assert "Example evaluator" in list(iter(workflow_execution))

    with pytest.raises(NotImplementedError):
        collection.register(workflow_execution)

    with pytest.raises(NotImplementedError):
        collection.update(workflow_execution)


def test_build_new_execution(collection, predictor_evaluation_execution_dict):
    # Given
    workflow_execution_id = uuid.uuid4()
    build_data = predictor_evaluation_execution_dict.copy()
    build_data["id"] = str(workflow_execution_id)
    build_data["workflow_id"] = str(collection.workflow_id)

    # When
    execution = collection.build(build_data)

    # Then
    assert execution.uid == workflow_execution_id
    assert execution.project_id == collection.project_id
    assert execution.workflow_id == collection.workflow_id
    assert execution.session == collection.session


def test_workflow_execution_results(workflow_execution: PredictorEvaluationExecution, session, example_result_dict):
    # Given
    session.set_response(example_result_dict)

    # When
    results = workflow_execution["Example Evaluator"]

    # Then
    assert results.evaluator == PredictorEvaluationResult.build(example_result_dict).evaluator
    expected_path = '/projects/{}/predictor-evaluation-executions/{}/results'.format(
        workflow_execution.project_id,
        workflow_execution.uid,
    )
    assert session.last_call == FakeCall(method='GET', path=expected_path, params={"evaluator_name": "Example Evaluator"})


def test_trigger_workflow_execution(collection: PredictorEvaluationExecutionCollection, predictor_evaluation_execution_dict, session):
    # Given
    predictor_id = uuid.uuid4()
    session.set_response(predictor_evaluation_execution_dict)

    # When
    actual_execution = collection.trigger(predictor_id)

    # Then
    assert str(actual_execution.uid) == predictor_evaluation_execution_dict["id"]
    expected_path = '/projects/{}/predictor-evaluation-workflows/{}/executions'.format(
        collection.project_id,
        collection.workflow_id,
    )
    assert session.last_call == FakeCall(
        method='POST',
        path=expected_path,
        json=ModuleRef(str(predictor_id)).dump()
    )
