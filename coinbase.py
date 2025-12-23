import requests

response = requests.get(url="https://api.coinbase.com/v2/prices/BTC-EUR/spot")
print(response.status_code)
response.raise_for_status()
data = response.json()

print(data)