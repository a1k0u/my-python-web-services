from pydantic import BaseModel
from pydantic import Field
import uuid


class Category(BaseModel):
    name: str


class Product(BaseModel):
    id: uuid.UUID
    name: str = Field(description="Name of the product", min_length=1)
    description: str | None = Field(
        default=None, title="The description of the product", max_length=300
    )
    price: int = Field(ge=0, description="The price must be greater than zero")
    weight: float = Field(ge=0, description="The weight must be greater then zero")
    category: Category | None = None
    status: bool = True
