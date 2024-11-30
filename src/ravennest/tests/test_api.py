
from ravennest.api.coingecko import (
    get_current_price,
    get_historical_data,
    identify_blockchain,
)


class TestGetCurrentPrice:

    def test_valid_response(self, requests_mock):
        # Simuler une réponse valide de l'API
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {"bitcoin": {"eur": 50000}}
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        price = get_current_price("bitcoin", "eur")
        assert price == 50000, "Price should be 50000 for valid response"

    def test_valid_response_multiple_cryptos(self, requests_mock):
        mock_url = "https://api.coingecko.com/api/v3/simple/price"
        mock_response = {"bitcoin": {"eur": 50000}, "ethereum": {"eur": 4000}}
        requests_mock.get(mock_url, json=mock_response)

        price_btc = get_current_price("bitcoin", "eur")
        price_eth = get_current_price("ethereum", "eur")
        assert price_btc == 50000, "Price should be 50000 for Bitcoin"
        assert price_eth == 4000, "Price should be 4000 for Ethereum"

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
        assert data[0]["price"] == 69702.3087473573, "First price should match"

    def test_invalid_response_structure(self, requests_mock):
        # Simuler une réponse invalide de l'API
        mock_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        mock_response = {}  # Structure inattendue
        requests_mock.get(mock_url, json=mock_response)

        # Tester la fonction
        data = get_historical_data("bitcoin")
        assert data is None, "Data should be None for invalid response structure"

    def test_http_error(self, requests_mock):
        # Simuler une erreur HTTP (404 Not Found)
        mock_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        requests_mock.get(mock_url, status_code=404)

        # Tester la fonction
        data = get_historical_data("bitcoin")
        assert data is None, "Price should be None for HTTP error"


# class TestCalculatePortfolioValue:


class TestIDentifyBlockchain:

    def test_bitcoin_address(self):
        address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNas"
        result = identify_blockchain(address)
        assert result == "Bitcoin", "Should identify Bitcoin for a valid Bitcoin address"

    def test_ethereum_address(self, monkeypatch):
        address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

        monkeypatch.setattr("builtins.input", lambda _: "Ethereum")

        result = identify_blockchain(address)
        assert result == "Ethereum", "Should return 'Etehreum' for Ethereum/Binance Smart Chain"

    def test_tron_address(self):
        address = "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb"
        result = identify_blockchain(address)
        assert result == "TRON", "Should identify Tron for a valid Tron address"

    def test_unknown_address(self, monkeypatch):
        address = "abcdef123456"

        # Mock user input to simulate manual blockchain entry
        monkeypatch.setattr("builtins.input", lambda _: "CustomChain")

        result = identify_blockchain(address)
        assert result == "CustomChain", "Should return user-specified blockchain for unknown address"

    def test_ambiguous_address(self, monkeypatch):
        address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

        # Mock user input to resolve ambiguity
        monkeypatch.setattr("builtins.input", lambda _: "Ethereum")

        result = identify_blockchain(address)
        assert result == "Ethereum", "Should return user selection for ambiguous blockchain"
