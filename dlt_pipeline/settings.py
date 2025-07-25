import dlt
from datetime import datetime, timezone, timedelta

symbols = ["AAPL", "TSLA", "AMZN", "MSFT"]
today = datetime.now(timezone.utc).date() - timedelta(days=1)
end_date = f"{today}T00:00:00Z"

def headers():
    api_key = dlt.secrets["sources.credentials.API_KEY"]
    secret_key = dlt.secrets["sources.credentials.SECRET_KEY"]

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key
    }

    return headers


def retrive_daily_shares_parametrs():
   
    start_date = "1999-12-31T00:00:00Z"
    param = {
        "symbols" : ",".join(symbols),
        "start": start_date,
        "end": end_date,
        "limit":100,
        "sort":"asc"
    }
    return param



def retrive_daily_news_paramets():

    start_date = "2015-01-01T00:00:00Z"
    params = {
        "symbols":",".join(symbols),
        "start":start_date,
        "end":end_date,
        "sort":"desc"
    }

    return params