from cryptocurrency.model.transaction import Transactions
from cryptocurrency import db
from flask import jsonify
from flask_restx import marshal
from flask_sqlalchemy import SQLAlchemy
from cryptocurrency.dto.transaction_dto import TransactionDTO

# def get_transactions_by_user_id(user_id):
#     return Transactions.query.filter(Transactions.user_id == user_id).first()


def get_transactions_by_user_id(user_id):
    return marshal(Transactions.query.filter_by(user_id=user_id).all(), TransactionDTO.transaction),200


def get_all_transactions():
    return marshal(Transactions.query.all(), TransactionDTO.transaction), 200


def get_transaction(transaction_id):
    return marshal(Transactions.query.filter(Transactions.id == transaction_id).first(), TransactionDTO.transaction), 200


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


def get_transaction_id(transaction_id):
    return Transactions.query.get(transaction_id)
