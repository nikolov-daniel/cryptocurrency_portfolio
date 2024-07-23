import requests
import argparse
from dotenv import load_dotenv
import os

prices = None


#https://rest.coinapi.io/v1/exchangerate

class Crypto:
    def __init__(self, symbol, rate):
        self.symbol = symbol
        self.rate = rate


def convert(coin):
    return Crypto(coin["asset_id_quote"], coin["rate"])


def get_prices(currency):
    try:

        # parser = argparse.ArgumentParser()
        # parser.add_argument('--token', help='token, REQUIRED', required=True)
        # parser.add_argument('--url', help='url, REQUIRED', required=True)
        # parser.add_argument('--timeout', help='timeout', required=False)
        # parser.add_argument('--verify', help='verify', required=False)
        # parser.add_argument('--proxy_url', help='proxy_url', required=False)
        # args, unknown = parser.parse_known_args()
        #
        # base_url = args.url
        # url = f"{base_url}{currency}"

        load_dotenv()
        base_url = os.getenv("API_URL")
        url = f"{base_url}/{currency}"
        api_token = os.getenv("API_TOKEN")

        payload = {}
        headers = {
            'Accept': 'text/plain',
            'X-CoinAPI-Key': f'{api_token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        session = requests.Session()
        get_session = session.get(url, headers=headers, data=payload)
        #print(get_session)
        #response.raise_for_status()  # Raise an error for non-2xx re   sponses
        #print(json.dumps(get_session.json()))
        coins = get_session.json()
        coins = coins["rates"]

        return list(map(convert, coins))

    except Exception as e:
        print(e)


def save_prices():
    global prices
    prices = get_prices(currency="USD")


def get_prices_cache():
    global prices
    if prices is None:
        return get_prices("USD")
    return prices
#base_currency = "USD"
#get_prices(base_currency)


