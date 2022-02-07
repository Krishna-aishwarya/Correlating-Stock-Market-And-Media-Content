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
import csv

from tickers_extractor import get_ticker
    

def get_market_values(date, companies_n_stocks_names):
    # print("get Market")
    for company in companies_n_stocks_names:
        company = ' '.join(companies_n_stocks_names)
        ticker = get_ticker(company)
        if ticker is None:
            return None
        data = yf.download(tickers=companies_n_stocks_names, interval = '1h', start = date - timedelta(hours=6), end = date + timedelta(hours=4))
        fig = go.Figure(data = [go.Candlestick(x=data.index, open = data['Open'],high = data['High'],low=data['Low'],close = data['Close'])])
        fig.show()
    

    
    
    #get_market_values(datetime.now() - timedelta(days=10), "BTC")
    

            

