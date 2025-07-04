

def flatten_daily_shares(stock_data):
    flatten_data = []
    for symbol, days in stock_data.items():
        if not symbol:
            continue

        for day in days:
            date = day["d"]

            if not date:
                continue

            if not day.get("c") or not day.get("o"):
                continue
            
            try:
                """
                    pick first entry from open list and last entry from close list
                """
                first_open = day['o'][0]  
                last_close = day['c'][-1]  

                if date and symbol:
                    flatten_data.append({
                        "id": f"{symbol}_{date}",
                        "symbol": symbol,
                        "date": date,
                        "open_price": first_open['p'],
                        "open_volume": first_open['s'],
                        "close_price": last_close['p'],
                        "close_volume": last_close['s']
                    })
            except Exception as e:
                print(f"Error ocured: {e}")

    return flatten_data