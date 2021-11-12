import requests
import json
import pandas as pd
from bitmex import bitmex


api_key = ''
api_secret = ''

test_key = ''
test_secret = ''

action = "BUY"
amount = 100

client = bitmex(test=False, api_key=api_key, api_secret=api_secret)

result = client.Quote.Quote_get(symbol="XBTUSD", reverse=True, count=1).result()
bid = result[0][0]['bidPrice'] - 10000
ask = result[0][0]['askPrice'] + 10000

#print (bid, ask)

pos = client.Position.Position_get().result()

pos_df = pd.DataFrame(pos[0])
pos_size = pos_df['currentQty'][0]
print (pos_size)

if action == "BUY":
	response = client.Order.Order_new(symbol='XBTUSD', ordType = "Limit", orderQty=amount, price=bid).result()
elif action == "SELL":
	response = client.Order.Order_new(symbol='XBTUSD', ordType = "Limit", orderQty=-amount, price=ask).result()