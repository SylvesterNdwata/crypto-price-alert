import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("PASSWORD")

to_email = os.environ.get("TO_ADDR")


def bitcoin_price():
    response = requests.get(url="https://api.binance.com/api/v3/ticker/price", params={"symbol": "BTCEUR"})
    response.raise_for_status()
    data = response.json()
    return data["price"]
    
def ethereum_price():
    response = requests.get(url="https://api.binance.com/api/v3/ticker/price", params={"symbol": "ETHEUR"})
    response.raise_for_status()
    data = response.json()
    return data["price"]

bit_price = bitcoin_price()
eth_price = ethereum_price()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=to_email,
        msg=f"Subject:CRYPTO PRICE ALERT\n\nThe current bitcoin price is {bit_price}\nThe current ethereum price is {eth_price}"
    )
    