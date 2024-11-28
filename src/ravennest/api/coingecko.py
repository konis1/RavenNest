# import os
from dotenv import load_dotenv
from typing import List, Dict

import requests

# Load environment variables from .env file
load_dotenv()


def get_current_price(crypto: str, currency: str = "eur") -> float | None:
    """
    Fetches the current price of a cryptocurrency in a specified currency.

    Args:
        crypto (str): The ID of the cryptocurrency (e.g., "bitcoin").
                      This should match the ID used by the CoinGecko API.
        currency (str, optional): The target currency for the price (default is "eur").
                                  Examples include "usd", "eur", "gbp", etc.

    Returns:
        float | None: The current price of the cryptocurrency in the specified currency,
                      or None if an error occurs or the response is invalid.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request returns a status code indicating an error.
        requests.exceptions.RequestException: For any issues during the request process (e.g., network errors).

    Notes:
        - This function uses the CoinGecko API (https://www.coingecko.com/).
        - Ensure the provided `crypto` matches a valid CoinGecko ID.
        - The function includes basic error handling and prints error messages for debugging purposes.
    """

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
    """
    Fetches historical price data for a cryptocurrency.

    Args:
        crypto (str): ID of the cryptocurrency (e.g., "bitcoin").
        currency (str): Target currency (default: "eur").
        days (int): Number of days to fetch data for (e.g., 30).

    Returns:
        List[Dict] | None: List of dictionaries containing 'date' and 'price',
    """

    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart"

    params: Dict[str, str] = {
        "vs_currency": currency,  # Target currency
        "days": days
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "prices" in data:
            return [
                {"date": point[0], "price": point[1]}
                for point in data["prices"]
            ]
        else:
            print(f"Missing 'prices' in API response for {crypto} in {currency}")
            return None
    except requests.exceptions.HTTPError:
        print(f"HTTP error fetching data: {response.status_code} {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"error fetching data:{e}")
        return None


def calculate_portfolio_value(
        portfolio: Dict[str, float],
        currency: str = "eur"
        ) -> tuple[float, Dict[str, float]]:
    """
    Calculate the total value of a cryptocurrency portfolio and provide a detailed breakdown.

    Args:
        portfolio (Dict[str, float]): A dictionary where keys are cryptocurrency IDs
                                        (e.g., "bitcoin") and values are the quantities held.
        currency (str, optional): The target currency for valuation (default is "eur").

    Returns:
        tuple[float, Dict[str, float]]:
            - Total portfolio value as a float, rounded to 2 decimal places.
            - A dictionary containing the individual values of each cryptocurrency
                in the portfolio.

    Notes:
        - If the portfolio is empty, the function will return 0.0 for the total value
            and an empty dictionary.
        - If a cryptocurrency's price cannot be fetched, it will be skipped, and a
            warning will be printed.

    Example:
        >>> portfolio = {"bitcoin": 0.5, "ethereum": 2}
        >>> calculate_portfolio_value(portfolio, "usd")
        (54000.00, {"bitcoin": 25000.00, "ethereum": 29000.00})
    """

    if not portfolio:
        print("Portfolio is empty.")
        return 0.0
    detailed_values = {}
    total_value = 0
    for crypto, amount in portfolio.items():
        price = get_current_price(crypto, currency)
        if price is not None:
            detailed_values[crypto] = price * amount
            total_value += price * amount
        else:
            print(f"Could not fetch price for {crypto}")
    return total_value, detailed_values
