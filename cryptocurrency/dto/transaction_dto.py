from flask_restx import Namespace, fields


class TransactionDTO:
    api = Namespace('Transactions')

    transaction = api.model('GetTransaction', {
        "id": fields.Integer(),
        "user_id": fields.Integer(attribute="users.id"),
        "cryptocurrency": fields.String(required=True),
        "amount": fields.Float(required=True),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
        "transactionDate": fields.DateTime()
    })
    transaction_post = api.model('PostTransaction', {
        #"id": fields.Integer(),
        #"user_id": fields.Integer(attribute="users.id"),
        "cryptocurrency": fields.String(required=True),
        "amount": fields.Float(required=True),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
        #"transactionDate": fields.DateTime()
    })
    transaction_put = api.model('PutTransaction', {
        # "id": fields.Integer(),
        # "user_id": fields.Integer(attribute="users.id"),
        "cryptocurrency": fields.String(),
        "amount": fields.Float(),
        "transactionType": fields.String(),
        "transactionPrice": fields.Float(),
        # "transactionDate": fields.DateTime()
    })
