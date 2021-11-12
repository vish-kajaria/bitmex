import requests
import json
import pandas as pd
from bitmex import bitmex


api_key = ''
api_secret = ''

test_key = ''
test_secret = ''

client = bitmex(test=False, api_key=api_key, api_secret=api_secret)

quote_1 = client.Quote.Quote_get(symbol="DOGEUSDT", reverse=True, count=1).result()
quote_2 = client.Quote.Quote_get(symbol="ETHUSD", reverse=True, count=1).result()

ask = float(quote_1[0][0]['askPrice'])
bid = float(quote_1[0][0]['bidPrice'])
mark_1 = (ask+bid)/2

ask = float(quote_2[0][0]['askPrice'])
bid = float(quote_2[0][0]['bidPrice'])
mark_2 = (ask+bid)/2

print ("Mark Price = " + str(round(mark_1/mark_2,10)) + " = " + str(mark_1) + "/" + str(mark_2))

pos = client.Position.Position_get().result()

pos_df = pd.DataFrame(pos[0])
#print (pos_df)
pos_1 = pos_df['avgEntryPrice'][1]
pos_2 = pos_df['avgEntryPrice'][0]
print ("Entry Price = " + str(round(pos_1/pos_2,10)) + " = " + str(pos_1) + "/" + str(pos_2))