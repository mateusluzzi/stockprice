# %%
import pandas as pd
import requests
from alpha_vantage.timeseries import TimeSeries
# %%

API_KEY = "X72MS62TNKB25VS7"
API_URL = "Https://www.alphavantage.co/query"
# %%
tickers = ['IBM','GOOGL']

# %%
def tickers_search(tickers_in):
    tickers = tickers_in
    aux = 0
    print('Tickers in:'+str(tickers_in))
    for ticker in tickers_in:
        ts = TimeSeries(key=API_KEY,output_format='pandas')
        ts,meta_data = ts.get_symbol_search(ticker)
        #ts = ts[ts['4. region'] == 'Brazil/Sao Paolo'] 
        ts['9. matchScore'] = pd.to_numeric(ts['9. matchScore'])  
        tickers[aux] = ts.loc[ts.groupby(['1. symbol'])['9. matchScore'].idxmax()]['1. symbol'].iloc[0]
        aux +=1
    print('Tickers out:'+str(tickers))
# %%
tickers_search(tickers) 
# %%
tickers
# %%
def intraday(tickers):
    intraday = pd.DataFrame()
    z = 0
    for s in tickers:
        params = {"function": "TIME_SERIES_INTRADAY",
                "symbol": tickers[z],
                "interval": "15min",
                "outputsize": "full",
                "datatype" : "json",
                "apikey":API_KEY}
        try:
            response = requests.get(API_URL, params)
            data = response.json()
            intraday2 = pd.DataFrame.from_dict(data["Time Series (15min)"],orient='index')
            intraday2 = intraday2.iloc[0:20000,:]
            intraday2['ticker'] = params['symbol']
            intraday = pd.concat([intraday,intraday2])
            print(intraday)
        except:
            print('Exceção')
            pass
        z += 1
# %%
intraday(tickers)
# %%
intraday
# %%
def daily_adjusted(tickers):
    daily_adjusted = pd.DataFrame()
    z = 0
    for s in tickers:    
        params = {"function":"TIME_SERIES_DAILY_ADJUSTED",
                "symbol" : tickers[z],
                "outputsize" : "compact",
                "apikey" : API_KEY}

        response = requests.get(API_URL, params)
        data = response.json()
        daily_adjusted2 = pd.DataFrame.from_dict(data["Time Series (Daily)"],orient='index')
        daily_adjusted2 = daily_adjusted2.iloc[0:20000,:]
        daily_adjusted2['ticker'] = params['symbol']
        daily_adjusted = pd.concat([daily_adjusted,daily_adjusted2])
        print(daily_adjusted)
        z += 1

# %%
daily_adjusted(tickers[:])
# %%

def overview(tickers):
        data = {}
        z = 0
        for s in tickers:
            params = {"function":"OVERVIEW",
                    "symbol" : tickers[z],
                    "apikey" : API_KEY}
            response = requests.get(API_URL, params)
            dict = response.json()
            data[s] = dict
            z += 1
        overview = pd.DataFrame.from_dict(data,orient='index').reset_index(drop=True)    
        return overview

# %%
overview(tickers)
# %%
overview