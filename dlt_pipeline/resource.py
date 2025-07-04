import requests
import dlt  
import requests
import os
from helpers import * 
from settings import *

def retrive_daily_shares():
    """
    Retrieve auction data from Alpaca between start_date and end_date
    for the given list of symbols.
    Ref: https://docs.alpaca.markets/reference/stockauctions-1
    """
   
    url = "https://data.alpaca.markets/v2/stocks/auctions"
    params = retrive_daily_shares_parametrs()
    header = headers()

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



@dlt.resource(write_disposition='merge', primary_key="id", name="raw_daily_stocks")
def virtual_trade_one():    
    yield from retrive_daily_shares()
