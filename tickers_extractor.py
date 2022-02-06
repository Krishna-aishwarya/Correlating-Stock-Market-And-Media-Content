import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_tickers():
    company_names = []
    company_tickers = []
    # print("hello")
    url = 'https://eoddata.com/stocklist/NYSE/A.htm'
    page = requests.get(url)
    soup = BeautifulSoup('page.text','lxml')
    table = soup.find('table',id='table')   
    headers = []
    # print("hello")
    print(table)
    return
    for i in table.find_all("td"):
        print(i)
    
if __name__ == '__main__':
    get_tickers()

    