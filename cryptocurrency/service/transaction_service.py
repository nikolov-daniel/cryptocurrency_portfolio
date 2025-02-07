from flask import session
from flask_restx import marshal
import functools
from cryptocurrency.dto.transaction_dto import TransactionDTO
from cryptocurrency.model.transaction import Transactions
from cryptocurrency.repository.transactions_repository import save_transaction, delete_transaction as repo_delete_transaction, get_transactions_by_user_id, get_transaction,get_transactions_by_user_id_unmarshalled
from cryptocurrency.service.user_service import get_user_by_username
from cryptocurrency.model.user import User
from cryptocurrency.service.util_service import parameter_update, get_transaction_id
from cryptocurrency.repository.db_util import flush_and_commit_changes
from cryptocurrency.service.crypto_service import get_prices_cache

transaction_dto = TransactionDTO.transaction


def validate_transaction_data(transaction):
    required_fields = ["cryptocurrency", "amount", "transactionType", "transactionPrice", "transactionCurrency"]
    for field in required_fields:
        if field not in transaction or not transaction[field]:
            return False, f"Missing required field: {field}"
    price = get_prices_cache("USD", transaction["cryptocurrency"])
    if not price:
        return False, "cryptocurrency not found"
    if price.rate != transaction["transactionPrice"]:
        return False, "price is not correct"
    return True, ""


def get_all_transactions_user_id(user_id):
    return get_transactions_by_user_id(user_id)


def get_all_transactions_user_id_unmarshalled(user_id):
    return get_transactions_by_user_id_unmarshalled(user_id)


def get_transaction_by_id(transaction_id):
    return get_transaction(transaction_id)


def create_transaction(transaction):
    username = session.get('username')
    if not username:
        return {"status": "error", "message": "User not logged in"}, 401

    user = get_user_by_username(username)
    if not user:
        return {"status": "error", "message": "User not found"}, 404

    is_valid, error_message = validate_transaction_data(transaction)
    if not is_valid:
        return {"status": "error", "message": error_message}, 422

    new_transaction = Transactions(
        #id=transaction["id"],
        user_id=user[0]["id"],
        cryptocurrency=transaction["cryptocurrency"],
        amount=transaction["amount"],
        transaction_type=transaction["transactionType"],
        transaction_price=transaction["transactionPrice"],
        transaction_currency=transaction["transactionCurrency"]

    )
    print("test")
    save_transaction(new_transaction)
    response_object = {
        "status": "success",
        "message": "Successfully created transaction"
    }
    return marshal(new_transaction, transaction_dto), 201


def delete_transaction(transaction_id):
    transaction = get_transaction(transaction_id)
    if not transaction:
        return {"status": "error", "message": "Transaction not found"}, 404

    repo_delete_transaction(transaction)
    return {"status": "success", "message": "Successfully deleted transaction"}, 200


def update_transaction(data, transaction_id):
    transaction = get_transaction_id(transaction_id)
    if not transaction:
        return {"status": "error", "message": "Transaction not found"}, 404

    user = get_user_by_username(data.get('username'))
    if not user:
        return {"status": "error", "message": "User not found"}, 404

    is_valid, error_message = validate_transaction_data(data)
    if not is_valid:
        return {"status": "error", "message": error_message}, 422

    parameter_update(obj=transaction, param_name='amount', old_value=transaction.amount, new_value=data.get('amount'))
    parameter_update(obj=transaction, param_name='cryptocurrency', old_value=transaction.cryptocurrency, new_value=data.get('cryptocurrency'))
    parameter_update(obj=transaction, param_name='transaction_type', old_value=transaction.transaction_type, new_value=data.get('transaction_type'))
    parameter_update(obj=transaction, param_name='transaction_price', old_value=transaction.transaction_price, new_value=data.get('transaction_price'))
    #parameter_update(obj=transaction, param_name='user_id', old_value=transaction.user_id, new_value=user.id)

    #TransactionDTO.transaction_put(transaction)
    flush_and_commit_changes()
    return marshal(transaction, transaction_dto), 200


def calculate_prices(transaction):
    portfolio_value = transaction["transaction_price"]*transaction["amount"]
    current_price = get_prices_cache(transaction["transaction_currency"], transaction["cryptocurrency"])
    current_value = transaction["amount"]*current_price
    return {"current": portfolio_value, "change": current_value}


def calculate_total(new, old):
    return {"current": new.value+old.value, "change": new.current+old.current}

def get_portfolio(user_id):
    transactions = get_all_transactions_user_id_unmarshalled(user_id)
    print(list(transactions))
    calculated = map(calculate_prices, transactions)
    return functools.reduce(calculate_total,calculated, {"current": 0, "change":0})