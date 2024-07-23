from cryptocurrency import db
from cryptocurrency.repository.db_util import rollback_and_close


def invalid_data_exception_handler(e):

    rollback_and_close()
    return {"errorMessage": e.args[0]}, 404


def not_logged_in_exception_handler(e):

    rollback_and_close()
    return {"errorMessage": e.args[0]}, 401


def handle_other_error(e):
    rollback_and_close()
    return {"errorMessage": e.args[0]}, 422

