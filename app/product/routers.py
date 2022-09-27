import uuid

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.product.contracts import Product
from app.product.contracts import Categoty
import app.db.method as request


router = APIRouter(prefix="/product")


@router.get("/all")
async def get_all_products():
    items = request.get_products()
    return {"products": items}, 200


@router.get("/all/categories")
async def get_all_categories():
    ...


@router.post("/add/category")
async def add_category(item: Categoty):
    ...


@router.post("/add")
async def add_products(item: Product):
    request.add_product(item)
    return JSONResponse({"code": 200}), 200


@router.put("/update/{product_id}")
async def update_product(item_id: uuid.UUID, item: Product):
    request.update_product(item_id, item)
    return JSONResponse({"code": 200}), 200  # TODO: if product doesn't exist


@router.delete("/delete/{product_id}")
async def delete_product(item_id: uuid.UUID):
    request.delete_product(item_id)
    return JSONResponse({"code": 200})
