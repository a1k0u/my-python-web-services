import pytest
from copy import deepcopy
from app.db.connection import __init_database
from app.product.contracts import Product
import app.db.method as request
from dataclasses import dataclass

batches = [
{
      "name": "Sup",
      "description": "So delicious!",
      "price": 123,
      "weight": 500,
      "category": {
        "name": "First course",
      },
      "status": 1
},
{
      "name": "Boom!",
      "description": "Wow!",
      "price": 100,
      "weight": 300,
      "category": {
        "name": "Second course",
      },
      "status": 0
}
]


@dataclass
class BatchUnit:
    batch: dict
    code: int


@pytest.fixture
def clear_database():
    request.__delete_tables()


@pytest.mark.parametrize("product", [BatchUnit(batch, 200) for batch in batches])
def test_product_methods(product):
    request.__delete_tables()
    code, response = request.add_product(Product(**product.batch))
    assert code == product.code
    assert response is None

    code, products = request.get_products()
    assert len(products) == 1

    product_id = products[0].id
    updated_batch = deepcopy(product.batch)
    updated_batch["name"] = "Updated_batch"

    # code, response = request.update_product(product_id, updated_batch)
    #assert code == 200

    #code, products = request.get_products()
    #assert products[0]["name"] == updated_batch["name"]

    code, response = request.delete_product(product_id)
    assert len(request.get_products()[1]) == 0
    assert code == 200
