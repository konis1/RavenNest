# Crypto Portfolio Manager

## **Overview**
Crypto Portfolio Manager is a Python-based application designed to help users track and analyze their cryptocurrency portfolios. The project leverages the CoinGecko API to fetch real-time and historical price data for cryptocurrencies, calculate portfolio values, and provide detailed insights.

---

## **Features**

### **Completed Sprints**
1. **Real-Time Price Fetching (Sprint 1)**:
   - Retrieve the current price of any cryptocurrency in a specified currency using the CoinGecko API.
   - Handle errors gracefully if the cryptocurrency ID is invalid or the API is unavailable.

2. **Historical Data Retrieval (Sprint 2)**:
   - Fetch historical price data for a cryptocurrency over a specified time period (e.g., 30 days).
   - Return data in a structured format for further analysis or visualization.
   - Handle invalid or incomplete responses from the API.

3. **Portfolio Value Calculation (Sprint 3)**:
   - Calculate the total value of a cryptocurrency portfolio based on the quantities held and current market prices.
   - Provide a detailed breakdown of the value contributed by each cryptocurrency in the portfolio.
   - Handle scenarios where price data for certain cryptocurrencies is unavailable.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- Pip for package management

### **Setup**
1. Clone the repository:
   ```bash
   git clone git@github.com:konis1/RavenNest.git
   cd RavenNest
   ```

2. Install the required dependencies:

3. Create a `.env` file (if needed) for storing API keys or other configuration details (optional).

---

## **Usage**

### **Functions**

#### **1. Get Current Price**
Fetch the current price of a cryptocurrency in a specified currency.

```python
from ravennest.api.coingecko import get_current_price

price = get_current_price("bitcoin", "usd")
print(price)  # Example output: 50000.75
```

#### **2. Get Historical Data**
Retrieve historical price data for a cryptocurrency over a given period.

```python
from ravennest.api.coingecko import get_historical_data

data = get_historical_data("bitcoin", "usd", 30)
print(data)
# Example output: [{"date": 1638307200000, "price": 50000}, ...]
```

#### **3. Calculate Portfolio Value**
Calculate the total value of a portfolio and get a detailed breakdown of individual contributions.

```python
from ravennest.api.coingecko import calculate_portfolio_value

portfolio = {"bitcoin": 0.5, "ethereum": 2}
total_value, detailed_values = calculate_portfolio_value(portfolio, "usd")

print(total_value)  # Example output: 58000.00
print(detailed_values)
# Example output: {"bitcoin": 25000.00, "ethereum": 8000.00}
```

---

## **Testing**

Run the test suite using `pytest` to verify the functionality:
```bash
pytest tests/
```

Tests include:
- Valid and invalid responses for `get_current_price`.
- Handling of empty or partial data in `get_historical_data`.
- Edge cases for `calculate_portfolio_value`.

---

## **Roadmap**

### **Upcoming Features**
- **Integration with Wallet Addresses**:
  - Automatically retrieve balances from blockchain APIs (e.g., Etherscan).
- **Support for Multi-Currency Portfolios**:
  - Calculate portfolio values across multiple fiat currencies.
- **Eventual CLI Interface**:
  - Enable users to interact with the application via a command-line tool.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
