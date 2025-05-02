import requests 
from .models import BitcoinPrice

def fetch_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        price = data['bitcoin']['usd']
        BitcoinPrice.objects.create(price_usd=price)
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error fetching Bitcoin price: {e}")