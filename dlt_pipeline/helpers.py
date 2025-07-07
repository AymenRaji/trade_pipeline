

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



def flatten_daily_news(news):
    all_news = []
    for new in news:
        primary_id = new["id"]
        if primary_id:
            data = {
                "author": new.get("author", ""),
                "content": new.get("content", ""),
                "created_at": new.get("created_at", ""),
                "headline": new.get("headline", ""),
                "id": primary_id,
                "source":new.get("source", ""),
                "summary":new.get("summary", ""),
                "symbols":new.get("symbols", []),
                "updated_at":new.get("updated_at", ""),
                "url":new.get("url", "")
            }
            all_news.append(data)
    
    return all_news