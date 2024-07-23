from flask import session
from flask_restx import marshal
from cryptocurrency.dto.transaction_dto import TransactionDTO
from cryptocurrency.model.transaction import Transactions
from cryptocurrency.repository.transactions_repository import save_transaction
from cryptocurrency.repository import transactions_repository

transaction_dto = TransactionDTO.transaction


def get_all_transactions(user_id):
    return transactions_repository.get_transactions_by_user_id(user_id)


def get_transaction(transaction_id):
    return transactions_repository.get_transaction(transaction_id)


def create_transaction(transaction):
    new_transaction = Transactions(
        user_id=transaction["user_id"],
        cryptocurrency=transaction["cryptocurrency"],
        amount=transaction["amount"],
        transaction_type=transaction["transaction_type"],
        transaction_price=transaction["transaction_price"],
        transaction_date=transaction["transaction_date"]
    )
    save_transaction(new_transaction)
    response_object = {
        "status": "success",
        "message": "successfully imported transaction"
    }
    return response_object, 201

    #return transactions_repository.create_transaction(transaction)


def update_transaction(transaction):
    u_transaction = transaction(
        user_id=transaction["user_id"],
        cryptocurrency=transaction["cryptocurrency"],
        amount=transaction["amount"],
        transaction_type=transaction["transaction_type"],
        transaction_price=transaction["transaction_price"],
        transaction_date=transaction["transaction_date"]
    )
    update_transaction(u_transaction)
    response_object = {
        "status": "success",
        "message": "successfully updated transaction"
    }
    return response_object, 201
    #return transactions_repository.update_transaction(transaction)


def delete_transaction(transaction):
    transactions_repository.delete_transaction(transaction)
