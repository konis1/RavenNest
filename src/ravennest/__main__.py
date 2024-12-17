from ravennest.api.coingecko import get_current_price, fetch_cryptos_below_ath

if __name__ == "__main__":
    crypto = "solana"
    price = get_current_price(crypto)

    if price is not None:
        print(f"The current price of {crypto} is {price}€")
    else:
        print(f"Failed to fetch the price of {crypto}.")

    percentage_below = 30  # Exemple : 30% inférieur à l'ATH
    cryptos = fetch_cryptos_below_ath(percentage_below)

    print(f"Cryptos dont la valeur est {percentage_below}% en dessous de leur ATH :\n")
    for idx, crypto in enumerate(cryptos[:10], 1):
        print(f"{idx}. {crypto['name']} ({crypto['symbol']}) - Prix actuel: ${crypto['current_price']}, ATH: ${crypto['ath']}, Market Cap: ${crypto['market_cap']}, Baisse: {crypto['drop_percentage']}%")

