import string
import requests

import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd
from bs4 import BeautifulSoup

from company_names_extractor import get_companies_and_stocks_names
from market_data_extractor import get_market_values  


def twitter_scraper(user):
    # Creating list to append tweet data
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()): #declare a username 
        today_date = datetime.datetime.now()
        if i>100:
            break
        if tweet.date.replace(tzinfo=None) >= today_date - datetime.timedelta(days=3):
            continue
        
        # print(dir(tweet))---- To see the available arguements and methods in the object
        companies_n_stocks_names = get_companies_and_stocks_names(tweet.content)
        
        # Do not append the rows where the companies and stocks List is empty
        if len(companies_n_stocks_names) == 0:
            continue
        
        market_df = get_market_values(tweet.date, companies_n_stocks_names)
        if market_df is None:
            continue
        
        tweets_list1.append([tweet.date,tweet.user.username,tweet.content,tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.retweetCount, tweet.url, companies_n_stocks_names]) #declare the attributes to be returned
        
        # Creating a dataframe from the tweets list above 
        tweets_df1 = pd.DataFrame(tweets_list1, columns=['Date','Username','Content','LikeCount','QuoteCount','ReplyCount','RetweetCount', 'URL','Companies and Stocks names'])
        break

    return tweets_df1
    
def get_tweets_from_users():
    user_list = ['potus']
    
    for user in user_list:
        user_info_df = twitter_scraper(user)
        user_info_df.to_csv(f'CSVFiles/{user}.csv')
    
    
    
if __name__ == "__main__":
    get_tweets_from_users()