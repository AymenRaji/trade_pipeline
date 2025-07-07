import requests
import dlt  
import requests
import os
from .helpers import * 
from .settings import *


header = headers()

def retrive_daily_shares():
    """
    Retrieve auction data from Alpaca between start_date and end_date
    for the given list of symbols.
    Ref: https://docs.alpaca.markets/reference/stockauctions-1
    """
   
    url = "https://data.alpaca.markets/v2/stocks/auctions"
    params = retrive_daily_shares_parametrs()
    

    all_flatten_data = []
    while True:

        response = requests.get(url, headers=header, params=params)
        response_json = response.json()
        auctions = response_json.get("auctions", [])

        if auctions:
            print(auctions)
            flatten_data = flatten_daily_shares(auctions)
            all_flatten_data.append(flatten_data)


        next_token = response_json.get("next_page_token", None)
        if next_token == None:
            break
        else:    
            params["page_token"] = next_token

        print(all_flatten_data)

    return all_flatten_data


def retrive_daily_news():

    params = retrive_daily_news_paramets()
    url = "https://data.alpaca.markets/v1beta1/news"

    all_news = []
    while True:
        response = requests.get(url, headers=header, params=params)

        response_json = response.json()
        news = response_json.get("news", [])
        if news:
            flattened_news = flatten_daily_news(news)
            all_news.append(flattened_news)

        next_page = response_json.get("next_page_token", "")
        if next_page:
            params["page_token"] = next_page
        else:
            break

    return all_news
    


@dlt.resource(
    write_disposition='merge', 
    primary_key="id", 
    name="raw_daily_stocks"
)
def virtual_trade_one():    
    yield from retrive_daily_shares()

@dlt.resource(
    write_disposition='merge', 
    primary_key="id", 
    name="raw_daily_news", 
    columns={"symbols": {"data_type": "json", "nullable": True}}
)
def daily_news():    
    yield from retrive_daily_news()



@dlt.source
def daily_share_statistics():
    return virtual_trade_one(), daily_news()

