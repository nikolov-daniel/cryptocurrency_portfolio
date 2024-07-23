from flask_restx import Namespace, fields


class CryptoDTO:

    api = Namespace('Crypto')

    crypto = api.model('GetCrypto', {
        "symbol": fields.String(),
        "rate": fields.Float()
    })
