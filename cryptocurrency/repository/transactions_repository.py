from cryptocurrency.model.transaction import Transactions
from cryptocurrency import db
from flask_sqlalchemy import SQLAlchemy


def get_transactions_by_user_id(user_id):
    return Transactions.query.filter(Transactions.user_id == user_id).first()


def get_transaction(transaction_id):
    return Transactions.query.filter(Transactions.id == transaction_id).first()


def save_transaction(transaction):
    db.session.add(transaction)
    db.session.commit()
    return transaction


def update_transaction(transaction):
    db.session.commit()
    return transaction


def delete_transaction(transaction):
    db.session.delete(transaction)
    db.session.commit()

