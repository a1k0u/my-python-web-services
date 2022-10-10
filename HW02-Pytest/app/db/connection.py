"""
Mock database made by shelve.

In future will use sqlalchemy with
async requests to data base.

Run this module first to init db.
"""

import shelve
from typing import Callable
from typing import Any


db_url = "/home/a1k0u/Documents/python-webservices-autumn-2022/app/db/database"


def db_connection(function: Callable):
    def wrapper(*args, **kwargs) -> (int, Any):
        with shelve.open(db_url, writeback=True) as db:
            code, res = 200, None

            try:
                res = function(db, *args, **kwargs)
            except IndexError:
                code = 404

        return code, res

    return wrapper


@db_connection
def __init_database(db, admin: int | None = None):
    db["product"] = []
    db["order"] = []
    db["telegram"] = [admin]


if __name__ == "__main__":
    __init_database()
