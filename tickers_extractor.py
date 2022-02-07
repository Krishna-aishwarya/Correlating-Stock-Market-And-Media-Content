import requests
import pandas as pd
from bs4 import BeautifulSoup
from Levenshtein import distance as levenshtein_distance

def get_ticker(company_name):
    # print("get ticker")
    df_nasdaq = pd.read_csv ('CSVFiles/nasdaq_screener_1644016190208.csv')
    # print(company_name)
    # return
    company_name_fromCSV = ""
    ticker = ""
    distance = len(company_name)
    for index,row in df_nasdaq.iterrows():
        # print(row['Name'])
        lvstn_dist = levenshtein_distance(company_name, row['Name'])
        if(lvstn_dist <= distance):
            distance = lvstn_dist
            company_name_fromCSV = row["Name"]
    return df_nasdaq.loc[company_name_fromCSV]['Symbol']
    
    

if __name__ == "__main__":
    get_ticker("Apple") 