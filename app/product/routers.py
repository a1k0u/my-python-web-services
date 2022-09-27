from fastapi import APIRouter, Path, Body, Query
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

import uuid

from app.product.contracts import Product
import app.db.method as request


router = APIRouter(prefix="/product")


@router.get("/all")
async def get_all_products(status: bool | None = Query(None)):
    code, response = request.get_products(status)
    return {"products": response}


@router.post("/add")
async def add_products(item: Product) -> JSONResponse:
    request.add_product(item)
    return JSONResponse({"message": "ok"}, status_code=200)


@router.put("/update/{item_id}")
async def update_product(
    item_id: uuid.UUID = Path(title="The ID of the item to get"),
    item: Product = Body(embed=True),
) -> JSONResponse:

    code, response = request.update_product(item_id, item)
    if code == 404:
        raise HTTPException(detail="Product doesn't find", status_code=404)
    return JSONResponse({"code": code})


@router.delete("/delete/{item_id}")
async def delete_product(
    item_id: uuid.UUID,
) -> JSONResponse:

    code, response = request.delete_product(item_id)
    if code == 404:
        raise HTTPException(detail="Product doesn't find", status_code=404)
    return JSONResponse({"msg": "ok"}, status_code=200)
