import uuid

import pytest
from copy import deepcopy
from app.db.connection import __init_database
from app.product.contracts import Product
import app.db.method as request
from dataclasses import dataclass

batches = [
    {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66a111",
        "name": "Sup",
        "description": "Delicious",
        "price": 234,
        "weight": 300,
        "category": {
            "name": "First course",
        },
        "status": 1,
    },
    {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66a222",
        "name": "Porridge",
        "description": "",
        "price": 100,
        "weight": 500,
        "category": {
            "name": "Second course",
        },
        "status": 0,
    },
    {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66a333",
        "name": "Apple",
        "description": "Green",
        "price": 300,
        "weight": 1000,
        "category": {
            "name": "First course",
        },
        "status": 0,
    },
]


@pytest.fixture
def clear_tables():
    request.__delete_tables()


def test_add_product(clear_tables):
    for batch in batches:
        code, response = request.add_product(Product(**batch))
        assert code == 200


@pytest.mark.parametrize("q, amount", [(True, 1), (False, 2), (None, 3)])
def test_get_products(q: bool, amount: int):
    code, response = request.get_products(q)
    assert len(response) == amount


@pytest.mark.parametrize(
    "id, expected_code",
    [
        (uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66a111"), 200),
        (uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66a222"), 200),
        (uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66a444"), 404),
    ],
)
def test_delete_product(id: uuid.UUID, expected_code: int):
    code, response = request.delete_product(id)
    assert code == expected_code


@pytest.mark.parametrize(
    "id, values, expected_code",
    [
        (uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66a333"), {"price": 55}, 200),
        (uuid.UUID("3fa85f64-5717-4562-b3fc-2c963f66a444"), {}, 404),
    ],
)
def test_update_product(id: uuid.UUID, values: dict, expected_code: int):
    code, response = request.update_product(id, values)
    assert code == expected_code


def test_foo():
    code, response = request.get_products()
    assert len(response) == 1
