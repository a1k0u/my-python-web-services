import datetime

from fastapi import APIRouter

from app.contracts import User

router = APIRouter()


@router.get("/")
async def read_index(name: str = "world"):
    """
    Returns welcome page with
    name from query parameters or
    default = "world".
    """

    return {"msg": f"Hello, {name}!"}


@router.get("/profile/{user_id}")
async def get_user_profile(user_id: int):
    """
    Returns user with define id by path url.
    """

    return {"msg": f"You try to get user with {user_id} id!"}


@router.post("/create")
async def create_user(user: User):
    """
    Returns information about
    user creation from request body.
    """

    user_info = user.dict()
    user_info["creation"] = datetime.datetime.now()

    return user_info
