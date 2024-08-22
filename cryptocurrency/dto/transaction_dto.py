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
        "transactionPrice": fields.Float(required=True,attribute="transaction_price"),
        "transactionDate": fields.DateTime(attribute="transaction_date"),
        "transactionCurrency": fields.String(required=True, attribute="transaction_currency")
    })
    transaction_post = api.model('PostTransaction', {
        "cryptocurrency": fields.String(required=True),
        "amount": fields.Float(required=True),
        "transactionType": fields.String(required=True),
        "transactionPrice": fields.Float(required=True),
        "transactionCurrency": fields.String(required=True)
    })
    transaction_put = api.model('PutTransaction', {
        "cryptocurrency": fields.String(),
        "amount": fields.Float(),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
        "transactionCurrency": fields.String(),
    })
    transaction_portfolio = api.model('GetTransaction', {
        "current": fields.Float(),
        "change": fields.Float()
    })
