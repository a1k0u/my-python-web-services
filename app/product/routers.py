import uuid

from fastapi import APIRouter, Path, Body
from fastapi.responses import JSONResponse
from app.product.contracts import Product
from app.product.contracts import Categoty
import app.db.method as request


router = APIRouter(prefix="/product")


@router.get("/all")
async def get_all_products():
    """
    get_all_products
        Returns all products from database.

    Returns:
        dict : {
            code: int,
            products: list[Products]
        }
    """

    code, response = request.get_products()
    return {"code": code, "products": response}


@router.get("/all/categories")
async def get_all_categories() -> None:
    ...


@router.post("/add/category")
async def add_category(item: Categoty) -> None:
    ...


@router.post("/add")
async def add_products(item: Product) -> JSONResponse:
    """
    add_products
        Adds product in a database.

    Args:
        item (Product)

    Returns:
        JSONResponse: {
            code: int
        }
    """

    code, response = request.add_product(item)
    return JSONResponse({"code": code})


@router.put("/update/{product_id}")
async def update_product(
    item_id: uuid.UUID = Path(title="The ID of the item to get"),
    item: Product = Body(embed=True),
) -> JSONResponse:
    code, response = request.update_product(item_id, item)
    return JSONResponse({"code": code})


@router.delete("/delete/{product_id}")
async def delete_product(
    item_id: uuid.UUID = Path(title="The ID of the item to get"),
) -> JSONResponse:
    code, response = request.delete_product(item_id)
    return JSONResponse({"code": code})
