import pytest
from app.db.connection import db_connection


@db_connection
def __get_columns(db):
    return dict(db).keys()


@pytest.mark.parametrize(
    "column, is_exist",
    [("product", True), ("order", True), ("telegram", True), ("abacaba", False)],
)
def test_db_creation(column: str, is_exist: bool):
    assert (column in __get_columns()[1]) == is_exist
