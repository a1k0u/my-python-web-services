import uuid
from app.db.connection import db_connection
from app.product.contracts import Product, Category


def __find_product(db, product_id: uuid.UUID) -> int:
    for i, product in enumerate(db["product"]):
        if product.id == product_id:
            return i
    raise IndexError


def __check_status(product_status, q_status) -> bool:
    return True if q_status is None else product_status == q_status


@db_connection
def get_products(db, status=None) -> list[Product]:
    return [product for product in db["product"] if __check_status(product.status, status)]


@db_connection
def add_product(db, item: Product) -> None:
    db["product"].append(item)


@db_connection
def update_product(db, product_id: uuid.UUID, item: Product) -> None:
    index = __find_product(db, product_id)
    db["product"][index] = db["product"][index].copy(update=item.__dict__)


@db_connection
def delete_product(db, product_id: uuid.UUID) -> None:
    index = __find_product(db, product_id)
    del db["product"][index]


@db_connection
def __delete_tables(db):
    for key in db.keys():
        db[key] = []
