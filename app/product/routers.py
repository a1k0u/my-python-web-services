from fastapi import APIRouter
from app.product.contracts import Product
from app.product.contracts import Categoty


router = APIRouter(prefix="/product")


@router.get("/all")
async def get_all_products():
    ...


@router.get("/all/categories")
async def get_all_categories():
    ...


@router.post("/add/category")
async def add_category(item: Categoty):
    ...


@router.post("/add")
async def add_products(item: list[Product]):
    ...


@router.put("/update/{product_id}")
async def update_product(product_id: int):
    return {"product_id": product_id}


@router.delete("/delete/{product_id}")
async def delete_product(product_id: int):
    return {"product_id": product_id}
