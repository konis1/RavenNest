from ravennest.api.coingecko import get_current_price

if __name__ == "__main__":
    crypto = "solana"
    price = get_current_price(crypto)

    if price is not None:
        print(f"The current price of {crypto} is {price}€")
    else:
        print(f"Failed to fetch the price of {crypto}.")
