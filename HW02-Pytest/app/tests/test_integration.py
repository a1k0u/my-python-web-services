import uuid

import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.db.method import __delete_tables
import json


temp_json = {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66a111",
    "name": "name2",
    "price": 100,
    "weight": 300,
}


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def clear_tables():
    __delete_tables()


def test_get_empty(client, clear_tables):
    response = client.get("/product/all")
    assert response.status_code == 200
    assert json.loads(response.content) == {"products": []}


@pytest.mark.parametrize(
    "values, expected_code",
    [
        ({}, 422),
        ({"name": "name1"}, 422),
        (temp_json, 200),
        (temp_json.copy().update(weigth=-100), 422),
        (temp_json.copy().update(price=-100), 422),
    ],
)
def test_add_product(client, values: dict, expected_code: int):
    response = client.post("/product/add", json=values)
    assert response.status_code == expected_code


@pytest.mark.parametrize(
    "item_id, values, expected_code",
    [
        (
            "3fa85f64-5717-4562-b3fc-2c963f66a111",
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66a111",
                "name": "Sup",
                "price": 200,
                "weight": 500,
            },
            200,
        ),
        ("3fa85f64-5717-4562-b3fc-2c963f66a222", temp_json, 404),
    ],
)
def test_update_product(client, item_id: uuid.UUID, values: dict, expected_code: int):
    response = client.put(f"/product/update/{item_id}", json=values)
    assert response.status_code == expected_code


@pytest.mark.parametrize(
    "item_id, expected_code",
    [
        ("3fa85f64-5717-4562-b3fc-2c963f66a111", 200),
        ("3fa85f64-5717-4562-b3fc-2c963f66a222", 404),
    ],
)
def test_delete_product(client, item_id: uuid.UUID, expected_code: int):
    response = client.delete(f"/product/delete/{item_id}")
    assert response.status_code == expected_code
