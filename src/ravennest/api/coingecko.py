# import os
from dotenv import load_dotenv
from typing import List, Dict

import requests

# Load environment variables from .env file
load_dotenv()


def get_current_price(crypto: str, currency: str = "eur") -> float | None:
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": crypto,  # CoinGecko ID for the cryptocurrency
        "vs_currencies": currency  # Target currency
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # Validate response structure
        if crypto in data and currency in data[crypto]:
            return data[crypto][currency]
        else:
            print(f"Invalid response: {data}")
            return None
    except requests.exceptions.HTTPError:
        print(f"HTTP error fetching data: {response.status_code} {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"error fetching data:{e}")
        return None


def get_historical_data(
        crypto: str,
        currency: str = "eur",
        days: int = 30
        ) -> List[Dict] | None:
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart"

    params: Dict[str, str] = {
        "vs_currencies": currency,  # Target currency
        "days": days
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status
        data = response.json()
        if "prices" in data:
            return [
                {"date: ": point[0], "price: ": point[1]}
                for point in data["prices"]
            ]
    except requests.exceptions.HTTPError:
        print(f"HTTP error fetching data: {response.status_code} {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"error fetching data:{e}")
        return None
