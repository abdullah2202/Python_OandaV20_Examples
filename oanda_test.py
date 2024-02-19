from env import api as api_details
import requests
# from oandapyV20 import API
# import oandapyV20.endpoints.instruments as instruments
# import v20
# import v20.instrument as instruments

#url = "https://api-fxpractice.oanda.com"
url = "https://api-fxtrade.oanda.com"

# access_token = api_details.oanda_token
# account_id = api_details.account_id
# client = API(access_token=access_token, environment="practice")

# params = {"granularity" : "M30", "count" : 20}
# r = instruments.InstrumentsCandles(instrument="XAU_USD", params=params)

# client.request(r)
# print(r.response)

headers = {"Authorization" : api_details.oanda_token, "Content-Type" : "application/json",}
headers = {}
auth = "Authorization : " + api_details.oanda_token
query = url + "/v3/instruments/GBP_JPY/candles?count=20&granularity=M30"
response = requests.get(query, headers={'Authorization' : ""})
# print(headers)
print(response.json())
# print(api_details.oanda)