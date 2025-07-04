import dlt

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
    symbols = ["AAPL", "TSLA", "AMZN", "MSFT"]
    start_date = "1999-12-31T00:00:00Z"
    end_date = "2025-07-03T00:00:00Z"
    param = {
        "symbols" : ",".join(symbols),
        "start": start_date,
        "end": end_date,
        "limit":100,
        "sort":"asc"
    }
    return param