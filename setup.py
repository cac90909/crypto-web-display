import datetime
from binance import Client

def log_in_client():
    
    a = open("api_key.txt","r")
    api_key = a.read().strip()

    b = open("api_secret.txt","r")
    api_secret = b.read().strip()

    a.close()
    b.close()

    client = Client(api_key, api_secret)
    print("Logged in")
    return client


def get_prices():
    #An example portfolio
    portfolio = {'ADABTC':'0','LTCBTC':'0','UNIBTC':'0','ETHBTC':'0'}
    client = log_in_client()
    tickers = client.get_ticker()

    for crypto in tickers:
        for asset in portfolio:
            if crypto['symbol'] == asset:
                portfolio[asset] = crypto['askPrice']
    
    return portfolio

def get_time():

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time