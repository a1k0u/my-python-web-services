import uuid
from enum import Enum
from pydantic import BaseModel


class Categoty(BaseModel):
    name: str


class Status(Enum):
    PRESENT = 1
    ENDED = 0


class Product(BaseModel):
    id: uuid.UUID | None = None
    name: str
    description: str | None = None
    price: int
    weight: float
    category: Categoty | None = None
    status: Status = Status.PRESENT
