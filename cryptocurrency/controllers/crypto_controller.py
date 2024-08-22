from flask import request
from flask_restx import Resource

from cryptocurrency.auth_decorator import authenticate
from cryptocurrency.dto.crypto_dto import CryptoDTO
from cryptocurrency.service.crypto_service import get_prices_cache

api = CryptoDTO.api

@api.route('/<currency>', methods=['GET'])
class CryptoController(Resource):

    @api.response(200, 'List of transactions', model=CryptoDTO.crypto)
    @api.marshal_with(CryptoDTO.crypto)
    def get(self, currency):
        #return get_prices(currency)
        return get_prices_cache(currency, None)

@api.route('/<currency>/<symbol>', methods=['GET'])
class CryptoController(Resource):


    @api.response(200, 'List of transactions', model=CryptoDTO.crypto)
    @api.marshal_with(CryptoDTO.crypto)
    def get(self, currency, symbol):
        #return get_prices(currency)

        return get_prices_cache(currency, symbol)





