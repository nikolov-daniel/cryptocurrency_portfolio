from functools import wraps

from flask import session

from cryptocurrency.constants import USER_NOT_LOGGED
from cryptocurrency.exceptions.exceptions import UserNotLoggedError


def authenticate(func):
    def wrapper(*args, **kwargs):
        username = session.get('username')

        if not username:
            raise UserNotLoggedError(USER_NOT_LOGGED)

        return func(*args, **kwargs)
    return wrapper
