import pytest
from workflows_engine.core.tasks import Flow
from workflows_engine import validators
from ..schema_validator import get_validator_for


@pytest.fixture
def flow():
    return Flow(name="main_flow")


def test_add_task_to_flow(flow):
    task = flow.add_task(
        task_type="jsonrpc",
        name="task",
        url="/endpoint/task/url",
        method="GET",
        payload_paths=[
            {"key": "$.arg1", "result_key": "$.arg1_result"},
            {"key": "$.arg2", "result_key": "$.arg2_result"},
        ],
        payload={"arg1_result": None, "arg2_result": None},
        response_path="$.response",
    )

    assert task in flow.tasks, "Tasks do not contain result of add_task"


def test_flow_to_dict(flow):
    task = flow.add_task(
        task_type="jsonrpc",
        name="task",
        url="/endpoint/task/url",
        preconditions=validators.is_equal(value_key="$.value", validator_value="a"),
        method="GET",
        payload_paths=[
            {"key": "$.arg1", "result_key": "$.arg1_result"},
            {"key": "$.arg2", "result_key": "$.arg2_result"},
        ],
        payload={"arg1_result": None, "arg2_result": None},
        response_path="$.response",
    )
    validator = get_validator_for("tasks/flow")
    validator.validate(flow.as_dict())
