prices={"toyota":"25000","mercedes":"40000","BMW":"38000"}
prices2=prices.pop("mercedes")
print(f"price of a mercedes is {prices2}")

latest=prices.popitem()
print(f"the latest car available is {latest}")
prices={"toyota":"25000","mercedes":"40000","BMW":"38000"}
added=prices.setdefault("AUDI",39000)
print(prices)