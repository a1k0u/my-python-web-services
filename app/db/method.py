import uuid

from app.db.connection import db_connection
from app.product.contracts import Product, Categoty


def __find_product(db, product_id: uuid.UUID) -> int:
    for i, product in enumerate(db["product"]):
        if product.id == product_id:
            return i

    return len(db["product"])


@db_connection
def get_products(db) -> list[Product]:
    return db["product"]


@db_connection
def add_product(db, item: Product) -> None:
    item.id = uuid.uuid1()
    db["product"].append(item)


@db_connection
def update_product(db, product_id: uuid.UUID, item: Product) -> None:
    index = __find_product(db, product_id)
    db["product"][index].update(item)


@db_connection
def delete_product(db, product_id: uuid.UUID) -> None:
    index = __find_product(db, product_id)
    del db["product"][index]


@db_connection
def __delete_tables(db):
    for key in db.keys():
        db[key] = []
