import unittest
from unittest.mock import patch

from cryptocurrency.model.transaction import Transactions
from cryptocurrency.model.user import User
from cryptocurrency.service import transaction_service
from cryptocurrency.service import user_service
from cryptocurrency.service.transaction_service import save_transaction, update_transaction


class CourseServiceTest(unittest.TestCase):
    USER_1 = User(id=1,
                  username='user21',
                  email='user21@email.com',
                  password='123234ffga')

    TRANSACTION_1 = Transactions(id=1,
                                 user_id=1,
                                 cryptocurrency="BTC",
                                 amount=1,
                                 transactionType="BUY",
                                 transactionPrice=5800,
                                 )

    POST_CREATE_DATA = {
        "username": "user21",
        "email": "user21@email.com",
        "password": "123234ffga"
    }

    POST_LOGIN_DATA = {
        "username": "user21",
        "password": "123234ffga"
    }

    @patch.object(user_service, "get_user_by_username",
                  return_value=USER_1)
    @patch.object(transaction_service, "create_transaction")
    def test_save_transaction_success(self,
                                      mock_add_transaction,
                                      mock_get_user_by_username):
        # Given
        data = self.POST_LOGIN_DATA

        # When
        result, code = save_transaction(data)

        # Then
        mock_get_user_by_username.assert_called_once_with(self.POST_LOGIN_DATA.get('username'))
        mock_add_transaction.assert_called_once()

        assert code == 201
        assert result['username'] == self.POST_LOGIN_DATA.get('username')

    @patch.object(user_service.get_user_by_username, "get_user_by_username",
                  return_value=None)
    @patch.object(transaction_service.save_transaction, "add_transaction")
    def test_save_transaction_error(self,
                                    mock_add_transaction,
                                    mock_get_user_by_username):
        # Given
        data = self.POST_LOGIN_DATA

        # When
        result, code = save_transaction(data)

        # Then
        mock_get_user_by_username.assert_called_once_with(self.POST_LOGIN_DATA.get('username'))
        mock_add_transaction.assert_not_called()

        assert code == 404
        assert result.get('errorMessage')

    @patch.object(transaction_service.get_transaction, "get_transaction_by_id",
                  return_value=TRANSACTION_1)
    @patch.object(user_service.get_user_by_username, "get_username",
                  return_value=USER_1)
    @patch.object(transaction_service, "parameter_update")
    def test_update_transaction_success(self,
                                        mock_parameter_update,
                                        mock_get_user_by_username,
                                        mock_get_transaction_by_id):
        # Give
        data = self.TRANSACTION_1
        name = 'Flask'

        # When
        result, code = update_transaction(data, name)

        # Then
        mock_get_transaction_by_id.assert_called_once_with(name)
        mock_get_user_by_username.assert_called_once_with(data['username'])
        mock_parameter_update.assert_has_calls([
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='user_id',
                               old_value=self.TRANSACTION_1.user_id,
                               new_value=data.get('user_id')),
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='cryptocurrency',
                               old_value=self.TRANSACTION_1.cryptocurrency,
                               new_value=data.get('cryptocurrency')),
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='amount',
                               old_value=self.TRANSACTION_1.amount,
                               new_value=data.get('amount')),
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='transaction_type',
                               old_value=self.TRANSACTION_1.transaction_type,
                               new_value=data.get('transaction_type')),
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='transaction_price',
                               old_value=self.TRANSACTION_1.transaction_price,
                               new_value=data.get('transaction_price')),
            unittest.mock.call(obj=self.TRANSACTION_1,
                               param_name='transaction_price',
                               old_value=self.TRANSACTION_1.transaction_price,
                               new_value=data.get('transaction_price')),
        ])
        assert code == 201
