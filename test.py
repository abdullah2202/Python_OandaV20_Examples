from env import api
import requests
    
url = "https://marketdata.tradermade.com/api/v1/live"

querystring = {"currency":"XAUUSD","api_key":api.key}

response = requests.get(url, params=querystring)

print(response.json())

# print(api.key)
                          


