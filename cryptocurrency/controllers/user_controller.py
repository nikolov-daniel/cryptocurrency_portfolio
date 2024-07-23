from flask import request
from flask_restx import Resource

from cryptocurrency.auth_decorator import authenticate
from cryptocurrency.dto.user_dto import UserDTO
from cryptocurrency.service.user_service import get_user_by_username, get_all_users, create_user, log_in_user, \
    log_out_user

api = UserDTO.api


@api.route('/', methods=['GET'])
@api.route('/<string:username>', methods=['GET'])
@api.route('/create', methods=['POST'])
class UserController(Resource):

    @api.response(200, 'List of users', model=UserDTO.user)
    @authenticate
    def get(self, username=None):
        if username:
            return get_user_by_username(username)
        return get_all_users()

    @api.expect(UserDTO.add_user, validate=True)
    @api.response(201, 'Created user', model=UserDTO.user)
    def post(self):
        data = request.json
        return create_user(data)


@api.route('/login', methods=['POST'])
class LogInUserController(Resource):

    @api.expect(UserDTO.login_user, validate=True)
    @api.response(201, 'Login successful', model=UserDTO.user)
    def post(self):
        data = request.json
        return log_in_user(data)


@api.route('/logout/<string:username>', methods=['POST'])
class LogOutUserController(Resource):

    @api.response(201, 'Logout successful', model=UserDTO.user)
    def post(self, username):
        return log_out_user(username)


