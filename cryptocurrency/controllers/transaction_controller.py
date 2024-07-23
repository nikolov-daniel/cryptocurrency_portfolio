from flask import request
from flask_restx import Resource

from cryptocurrency.auth_decorator import authenticate
from cryptocurrency.dto.transaction_dto import TransactionDTO
from cryptocurrency.service.transaction_service import get_all_transactions, get_transaction, save_transaction, update_transaction, \
    delete_transaction


api = TransactionDTO.api


@api.route('/transactions/<id>', methods=['GET'])
@api.route('/transactions', methods=['POST', "PUT", "DELETE"])
class TransactionController(Resource):

    @api.response(200, 'List of transactions', model=TransactionDTO.transaction)
    def get(self, id):
        return get_transaction(id)

    @api.expect(TransactionDTO.transaction, validate=True)
    @api.response(201, 'Created transactions', model=TransactionDTO.transaction)
    def post(self):
        data = request.json
        return save_transaction(data)

    @api.expect(TransactionDTO.transaction, validate=True)
    @api.response(201, 'Updated transactions', model=TransactionDTO.transaction)
    @api.response(404, 'Not found')
    @authenticate
    def put(self):
        data = request.json
        return update_transaction(data)

    @api.response(201, 'Deleted transactions', model=TransactionDTO.transaction)
    @api.response(404, 'Not found')
    @authenticate
    def delete(self, name):
        return delete_transaction(name)


@api.route('/transactions/all', methods=["GET"])
class TransactionAllController(Resource):
    @api.response(200, 'List of transactions', model=TransactionDTO.transaction)
    def get(self):
        return get_all_transactions(self)

