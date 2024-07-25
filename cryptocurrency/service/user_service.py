from flask import session
from flask_restx import marshal

from cryptocurrency.constants import DUPLICATE_USERNAME, DUPLICATE_EMAIL, USERNAME_OR_PASSWORD_MISSING, WRONG_PASSWORD
from cryptocurrency.dto.user_dto import UserDTO
from cryptocurrency.exceptions.exceptions import InvalidDataError
from cryptocurrency.model.user import User
from cryptocurrency.repository import user_repository, db_util, transactions_repository


user_dto = UserDTO.user


def get_user_by_username(username):
    user = user_repository.get_user_by_username(username)

    return marshal(user, user_dto), 200


def get_all_users():
    return marshal(user_repository.get_all_users(), user_dto), 200


def create_user(data):
    if user_repository.get_user_by_username(data['username']):
        raise InvalidDataError(DUPLICATE_USERNAME)

    if user_repository.get_user_by_email(data['email']):
        raise InvalidDataError(DUPLICATE_EMAIL)

    user = User(username=data['username'],
                email=data['email'])
    user.set_password(data['password'])

    db_util.save_data(user)
    return marshal(user, user_dto), 201


def log_in_user(data):

    user = None

    if 'username' not in data and 'email' not in data:
        raise InvalidDataError(USERNAME_OR_PASSWORD_MISSING)
    elif 'username' in data:
        user = user_repository.get_user_by_username(data['username'])
    else:
        user = user_repository.get_user_by_email(data['email'])

    if not user.check_password(data['password']):
        raise InvalidDataError(WRONG_PASSWORD)

    session['username'] = user.username

    return marshal(user, user_dto), 201


def log_out_user(username):
    user = user_repository.get_user_by_username(username)

    session.pop('username', None)
    return marshal(user, user_dto), 201
