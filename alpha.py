import requests
from env import api

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=' + api.alpha
r = requests.get(url)
data = r.json()

print(data)