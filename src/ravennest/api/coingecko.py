import os

import requests

API_KEY = os.getenv("COINGECKO_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set the \
        COINGECKO_API_KEY environment variable.")


def get_current_price(crypto: str, currency: str = "eur") -> float:
    url = "https://api.coingecko.com/api/v3/simple/price"

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "API_KEY"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data[crypto][currency]
    except requests.Exception.RequestException as e:
        print(f"error fetching data:{e}")
        return None


crypto = "solana"
price = get_current_price(crypto)

if price:
    print(f"The current price of {crypto} is {price}")
