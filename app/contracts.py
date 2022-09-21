from pydantic import BaseModel


class User(BaseModel):
    """Contract for user."""

    name: str
    bio: str | None = None
    age: int
    weight: float | None = None
