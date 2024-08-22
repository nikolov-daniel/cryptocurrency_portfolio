from flask import request, session
from flask_restx import Resource, marshal


from cryptocurrency.constants import USER_NOT_LOGGED
from cryptocurrency.exceptions.exceptions import UserNotLoggedError, InvalidDataError
from cryptocurrency.service.user_service import get_user_by_username_unmarshalled
from cryptocurrency.auth_decorator import authenticate
from cryptocurrency.dto.transaction_dto import TransactionDTO
from cryptocurrency.service.transaction_service import create_transaction, get_all_transactions_user_id, get_transaction, save_transaction, update_transaction, \
    delete_transaction, get_transaction_by_id, get_portfolio

transaction_dto = TransactionDTO.transaction
transaction_portfolio_dto = TransactionDTO.transaction_portfolio

api = TransactionDTO.api


@api.route('/', methods=['GET', 'POST', 'PUT'])
class TransactionController(Resource):

    @api.response(200, 'List of all transactions', model=TransactionDTO.transaction)
    @authenticate
    def get(self):
        username = session["username"]
        if username == None:
            raise UserNotLoggedError(USER_NOT_LOGGED)
        user = get_user_by_username_unmarshalled(username)
        return get_all_transactions_user_id(user.id)

    @api.expect(TransactionDTO.transaction_post, validate=True)
    @api.response(201, 'Created transactions', model=TransactionDTO.transaction)
    @authenticate
    def post(self, name=None):
        data = request.json
        return create_transaction(data)

    @api.expect(TransactionDTO.transaction_put, validate=True)
    @api.response(201, 'Updated transactions', model=TransactionDTO.transaction)
    @api.response(404, 'Not found')
    @authenticate
    def put(self, transaction_id):
        data = request.json
        return update_transaction(data, transaction_id)




@api.route('/<id>', methods=['GET', 'DELETE'])
class TransactionControllerById(Resource):

    @api.response(200, 'List of all transactions', model=TransactionDTO.transaction)
    @authenticate
    def get(self, id):
        print("asd")
        username = session["username"]
        if username == None:
            raise UserNotLoggedError(USER_NOT_LOGGED)
        user = get_user_by_username_unmarshalled(username)
        print("pred tr  id")
        get_transaction_by_id(id)
        transaction = get_transaction_by_id(id)

        if transaction is None:
            raise InvalidDataError()
        print("posle tr  id")
        #transaction = transaction[0]
        if transaction.user_id != user.id:
            raise InvalidDataError()
        return marshal(transaction, transaction_dto), 200

    @api.response(201, 'Deleted transactions', model=TransactionDTO.transaction)
    @api.response(404, 'Not found')
    def delete(self, id):

        return delete_transaction(id)

@api.route('/portfolio', methods=['GET'])
class TransactionController(Resource):
    @api.response(200, 'portfolio', model=TransactionDTO.transaction)
    @authenticate
    def get(self):
        username = session["username"]
        if username == None:
            raise UserNotLoggedError(USER_NOT_LOGGED)
        user = get_user_by_username_unmarshalled(username)
        return marshal(get_portfolio(user.id), transaction_portfolio_dto), 200


# ####################################################
# @api.route('/transactions/<id>', methods=['GET', 'POST'])
# @api.route('/transactions', methods=['POST', "PUT", "DELETE"])
# class TransactionController(Resource):
#
#     @api.response(200, 'List of transactions', model=TransactionDTO.transaction)
#     def get(self):
#         return get_all_transactions_user_id
#
#     @api.expect(TransactionDTO.transaction, validate=True)
#     @api.response(201, 'Created transactions', model=TransactionDTO.transaction)
#     def post(self):
#         data = request.json
#         return save_transaction(data)
#
#     @api.expect(TransactionDTO.transaction, validate=True)
#     @api.response(201, 'Updated transactions', model=TransactionDTO.transaction)
#     @api.response(404, 'Not found')
#     @authenticate
#     def put(self):
#         data = request.json
#         return update_transaction(data)
#
#     @api.response(201, 'Deleted transactions', model=TransactionDTO.transaction)
#     @api.response(404, 'Not found')
#     @authenticate
#     def delete(self, name):
#         return delete_transaction(name)
#
#
# @api.route('/transactions/all', methods=["GET"])
# class TransactionAllController(Resource):
#     @api.response(200, 'List of transactions', model=TransactionDTO.transaction)
#     def get(self):
#         return get_all_transactions_user_id(self)
