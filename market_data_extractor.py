from symtable import Symbol
from xmlrpc.client import DateTime
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from matplotlib.pyplot import *
import requests 

from icecream import ic
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Levenshtein import distance as levenshtein_distance
import csv


#def get_ticker (company_name):
def get_ticker():
    df_nasdaq = pd.read_csv ('CSVFiles/nasdaq_screener_1644016190208.csv',index_col='Name')
    for row in df_nasdaq.iterrows():
        
        
    print(df_nasdaq.loc["ATA Creativity Global American Depositary Shares"]['Symbol'])
    
    

# def get_market_values(date, companies_n_stocks_names):
#     # for company in companies_n_stocks_names:
    
#     # company = ' '.join(companies_n_stocks_names)
#     # ticker = getTicker("Apple")
#     # ic(ticker)
#     # ticker = getTicker(company)
#     # if ticker is None:
#     #     return None
#     print(companies_n_stocks_names)
#     return
#     data = yf.download(tickers=companies_n_stocks_names, interval = '1h', start = date - timedelta(hours=6), end = date + timedelta(hours=4))
#     # print(data)
#     # print(len(data))

#     fig = go.Figure(data = [go.Candlestick(x=data.index, open = data['Open'],high = data['High'],low=data['Low'],close = data['Close'])])
#     # fig.show()
    

if __name__ == "__main__":
    get_ticker()
    
    
    #get_market_values(datetime.now() - timedelta(days=10), "BTC")
    

            

