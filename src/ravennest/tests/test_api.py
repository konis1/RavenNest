
from ravennest.api.coingecko import get_current_price, get_historical_data


class TestGetCurrentPrice:

    def test_valid_response(self, requests_mock):
        # Simuler une réponse valide de l'API
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {"bitcoin": {"eur": 50000}}
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price == 50000, "Price should be 50000 for valid response"

    def test_invalid_response_structure(self, requests_mock):
        # Simuler une réponse invalide de l'API
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {}  # Structure inattendue
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price is None, "Price should be None for invalid response structure"

    def test_http_error(self, requests_mock):
        # Simuler une erreur HTTP (404 Not Found)
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        requests_mock.get(mock_url, status_code=404)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price is None, "Price should be None for HTTP error"


class TestGetHistoricalData:
    def test_get_historical_data_valid(self, requests_mock):
        mock_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

        mock_response = {"prices": [
            [1711843200000, 69702.3087473573],
            [1711929600000, 71246.9514406015],
        ]}
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        data = get_historical_data("bitcoin")
        assert len(data) == 2, "Expected two data points"
        # assert data["prices"[0][1] == 69702.3087473573, "First price should match"
