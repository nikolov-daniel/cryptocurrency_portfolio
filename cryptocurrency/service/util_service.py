from cryptocurrency.constants import USER_NOT_FOUND, TRANSACTION_NOT_FOUND
from cryptocurrency.exceptions.exceptions import InvalidDataError
from cryptocurrency.model.transaction import Transactions
from cryptocurrency.model.user import User
from cryptocurrency.repository import transactions_repository, user_repository


def parameter_update(obj, param_name, old_value, new_value):
    if new_value is not None and old_value != new_value:
        setattr(obj, param_name, new_value)
        return True
    return False


def get_user_by_username(username: str) -> User:
    user: User = user_repository.get_user_by_username(username)
    if not user:
        raise InvalidDataError(USER_NOT_FOUND)
    return user


def get_user_by_email(email: str) -> User:
    user: User = user_repository.get_user_by_email(email)
    if not user:
        raise InvalidDataError(USER_NOT_FOUND)
    return user


def get_transaction_id(transaction_id: str) -> Transactions:
    transaction: Transactions = transactions_repository.get_transaction(transaction_id)
    if not transaction:
        raise InvalidDataError(TRANSACTION_NOT_FOUND)
    return transaction
