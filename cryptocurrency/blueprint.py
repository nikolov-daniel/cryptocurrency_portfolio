from flask import Blueprint, render_template, Flask
from flask_restx import apidoc, Api

from cryptocurrency.controllers.transaction_controller import api as transaction_ns
from cryptocurrency.controllers.user_controller import api as user_ns
from cryptocurrency.controllers.crypto_controller import api as crypto_ns
from cryptocurrency.exceptions.exceptions import InvalidDataError, UserNotLoggedError
from cryptocurrency.exceptions.handlers import invalid_data_exception_handler, not_logged_in_exception_handler, \
    handle_other_error


blueprint = Blueprint('api', __name__)


@apidoc.apidoc.add_app_template_global
def swagger_static(filename):
    return "./swaggerui/{0}".format(filename)


api = Api(blueprint,
          title="Transactions API",
          version='0.0.1')


@api.documentation
def custim_ui():
    return render_template("swagger-ui.html", title=api.title, specs_url="./swagger.json")


api.add_namespace(transaction_ns, path='/transactions')
api.add_namespace(user_ns, path='/user')
api.add_namespace(crypto_ns, path='/crypto')


api.error_handlers[InvalidDataError] = invalid_data_exception_handler
api.error_handlers[UserNotLoggedError] = not_logged_in_exception_handler
api.error_handlers[Exception] = handle_other_error


