
from ravennest.api.coingecko import get_current_price, get_historical_data

import requests


class test_get_current_price():

    def test_valid_response(self, requests_mock):
        # Simuler une réponse valide de l'API
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {"bitcoin": {"eur": 50000}}
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price == 50000, "Price should be 50000 for valid response"

    def test_invalid_response_structure(requests_mock):
    # Simuler une réponse invalide de l'API
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {}  # Structure inattendue
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price is None, "Price should be None for invalid response structure"

    def test_http_error(requests_mock):
        # Simuler une erreur HTTP (404 Not Found)
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        requests_mock.get(mock_url, status_code=404)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price is None, "Price should be None for HTTP error"

    def test_request_exception(mocker):
        # Simuler une exception réseau
        mocker.patch(
            "requests.get",
            side_effect=requests.exceptions.RequestException("Network error")
            )

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price is None, "Price should be None for network exception"


class test_get_historical_data():
    def get_historical_data_valid(self, requests_mock):
        mock_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

        mock_response = {"prices": [
            [1711843200000, 69702.3087473573],
            [1711929600000, 71246.9514406015],
        ]}
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_historical_data("bitcoin")
        print(price)
