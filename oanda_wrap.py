from env import api as api_details
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments

access_token = api_details.oanda_token
account_id = api_details.account_id
client = API(access_token=access_token)

params = {'granularity' : 'M30', 'count' : 50, 'smooth' : True}

r = instruments.InstrumentsCandles(instrument="XAU_USD", params=params)
client.request(r)

count = 0
data = r.response
candles = data['candles']

for candle in candles:
   # print(candle['time'] + "---" + candle['mid']['o'] + " " + candle['mid']['h'] + " " + candle['mid']['l'] + " " + candle['mid']['c'])
   open = float(candle['mid']['o'])
   close = float(candle['mid']['c'])
   count = count + 1
   if (open-close)>0:
      print(str(count) + " - Bear Candle")
   else:
      print(str(count) + " - Bull Candle")
   

# print(data)
