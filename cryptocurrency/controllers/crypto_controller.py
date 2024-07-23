from flask import request
from flask_restx import Resource

from cryptocurrency.auth_decorator import authenticate
from cryptocurrency.dto.crypto_dto import CryptoDTO
from cryptocurrency.service.crypto_service import get_prices_cache

api = CryptoDTO.api

@api.route('/crypto/<currency>', methods=['GET'])
class CryptoController(Resource):

    @api.response(200, 'List of transactions', model=CryptoDTO.crypto)
    @api.marshal_with(CryptoDTO.crypto)
    def get(self, currency):
        #return get_prices(currency)
        return get_prices_cache()





