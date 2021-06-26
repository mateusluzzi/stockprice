# %%
import os
import pandas as pd
import requests

# %%

API = "APUO17BD0D08LYO3"

# %%
def TIME_SERIES_INTRADAY(symbol,interval):
    sym = "&symbol="+symbol
    interv = "&interval="+interval
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"+sym+interv+"&apikey="+API
    r = requests.get(url).json()
    del r['Meta Data']
    r = r['Time Series (5min)']
    data = pd.DataFrame.from_dict(r,orient='index')
    return data
# %%
TIME_SERIES_INTRADAY("UBER","5min")


