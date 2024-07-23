from crryptocurrency import create_app
from flask import Flask
import requests
import argparse
import json

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Numeric, DateTime, VARCHAR
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import time

from cryptocurrency.model.transactions import Transactions
from cryptocurrency.model.user import User


app = create_app('dev')
app.app_context().push()

from crryptocurrency.blueprint import blueprint

app.register_blueprint(blueprint)
app.app_context().push()


def get_prices(currency):
    try:

        parser = argparse.ArgumentParser()
        parser.add_argument('--token', help='token, REQUIRED', required=True)
        parser.add_argument('--url', help='url, REQUIRED', required=True)
        parser.add_argument('--timeout', help='timeout', required=False)
        parser.add_argument('--verify', help='verify', required=False)
        parser.add_argument('--proxy_url', help='proxy_url', required=False)
        args, unknown = parser.parse_known_args()

        base_url = args.url
        url = f"{base_url}{currency}"

        payload = {}
        headers = {
            'Accept': 'text/plain',
            'X-CoinAPI-Key': f'{args.token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        session = requests.Session()
        get_session = session.get(url, headers=headers, data=payload)
        #print(get_session)
        #response.raise_for_status()  # Raise an error for non-2xx responses
        print(json.dumps(get_session.json()))
    except Exception as e:
        print(e)


base_currency = "USD"
get_prices(base_currency)

if __name__ == '__main__':
    app.run(debug=True)