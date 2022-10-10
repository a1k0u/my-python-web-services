"""
Testing client on Python.
"""

import pytest
import app.client as client


@pytest.mark.parametrize(
    "task_count, task, error",
    [
        (3, "Сфотографируйтесь с первым попавшимся человеком", 1),
        (4, "Сфотографируй то, что вызывает у тебя улыбку", 1),
        (-1, "Validation error", 0),
        (20, "Изобрази удивление и поделись селфи", 1),
    ],
)
def test_get_task(task_count: int, task: str, error: bool):
    response = client.main(task_count=task_count)
    assert response.task == task and response.error == error
