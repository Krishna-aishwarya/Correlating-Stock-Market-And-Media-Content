import requests
import pandas as pd
from bs4 import BeautifulSoup
from fuzzywuzzy import process

def get_ticker(company_name):
    df_nasdaq = pd.read_csv ('CSVFiles/nasdaq_screener_1644016190208.csv')
    company_names_list_of_df_nasdaq = df_nasdaq["Name"]
    matching_df_nasdaq_company_name = process.extract(company_name, company_names_list_of_df_nasdaq, limit=1)
    
    for i in range(len(df_nasdaq)):
        if str(matching_df_nasdaq_company_name[0][0]) == df_nasdaq.loc[i,"Name"]:
            return df_nasdaq.loc[i,"Symbol"]



