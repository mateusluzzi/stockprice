# %%
import os
import pandas as pd
from pandas.core.accessor import register_dataframe_accessor
import requests
import json
import io
# %%

API_KEY = "APUO17BD0D08LYO3"
API_URL = "Https://www.alphavantage.co/query"
# %%
tickers = ['UBER']
# %%
def intraday(tickers):
    for s in tickers:
        z = 0
        params = {"function": "TIME_SERIES_INTRADAY",
                "symbol": tickers[z],
                "interval": "15min",
                "datatype" : "json",
                "apikey":API_KEY}
        response = requests.get(API_URL, params)
        data = response.json()
        data = pd.DataFrame.from_dict(data["Time Series (15min)"],orient='index')
        data['ticker'] = params['symbol']
        print(data)
        z += 1
# %%
intraday(tickers[:])


# data.columns = ['1. open','2. high']
# data.sort_values(['1. open','2. high'], input = True)
# data.reset_index(drop=True, inplace=True)
# data
# %%
def TIME_SERIES_INTRADAY(symbol,interval):
    for s in symbol:
        sym = "&symbol="+s
        interv = "&interval="+interval
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"+sym+interv+"&apikey="+API
        r = requests.get(url).json()
        del r['Meta Data']
        r = r['Time Series (5min)']
        data = pd.DataFrame.from_dict(r,orient='index')
        print(s)
        data['ticker'] = s
        return data
# %%
TIME_SERIES_INTRADAY(["JPSA."],"5min")

