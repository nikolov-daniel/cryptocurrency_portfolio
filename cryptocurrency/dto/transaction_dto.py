from flask_restx import Namespace, fields


class TransactionDTO:
    api = Namespace('Transactions')

    transaction = api.model('GetTransaction', {
        "id": fields.Integer(),
        "user_id": fields.Integer(),
        "cryptocurrency": fields.String(),
        "amount": fields.Float(),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
        "transactionDate": fields.DateTime()
    })
