import uuid
from enum import Enum
from pydantic import BaseModel
from pydantic import Field


class Categoty(BaseModel):
    name: str


class Status(Enum):
    PRESENT = 1
    ENDED = 0


class Product(BaseModel):
    id: uuid.UUID | None = None
    name: str
    description: str | None = Field(
        default=None, title="The description of the product", max_length=300
    )
    price: int = Field(
        gt=0, description="The price must be greater than zero"
    )
    weight: float = Field(
        gt=0, description="The weight must be greater then zero"
    )
    category: Categoty | None = None
    status: Status = Status.PRESENT
