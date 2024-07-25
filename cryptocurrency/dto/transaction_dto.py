from flask_restx import Namespace, fields
from cryptocurrency.model.transaction import TransactionType


class TransactionDTO:
    api = Namespace('Transactions')

    transaction = api.model('GetTransaction', {
        "id": fields.Integer(),
        "user_id": fields.Integer(attribute="user_id"),
        "cryptocurrency": fields.String(required=True),
        "amount": fields.Float(required=True),
        "transactionType": fields.String(required=True,attribute="transaction_type", enum=TransactionType._member_names_),
        "transactionPrice": fields.Float(attribute="transaction_price"),
        "transactionDate": fields.DateTime(attribute="transaction_date")
    })
    transaction_post = api.model('PostTransaction', {
        "cryptocurrency": fields.String(required=True),
        "amount": fields.Float(required=True),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
    })
    transaction_put = api.model('PutTransaction', {
        "cryptocurrency": fields.String(),
        "amount": fields.Float(),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
    })
