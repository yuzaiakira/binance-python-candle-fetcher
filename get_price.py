import requests
import pandas as pd
from datetime import datetime

# Edit this varibeles for customazing 
symbol = 'ETHUSDT'  # Trading pair
interval = '15m'    # 15-minute interval
start_year = 2017 # start time for get price


def fetch_candlestick_data(symbol, interval, start_time, end_time):
    url = "https://api.binance.com/api/v3/klines"
    all_data = []
    
    while start_time < end_time:
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_time,
            'endTime': end_time,
            'limit': 1000 
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if not data:
            break 
        
        all_data.extend(data)
        
        start_time = data[-1][0] + 1

    return all_data

end_time = int(datetime.now().timestamp() * 1000) 

csv_file_name =  f'{symbol}_15m_data_{start_year}_{datetime.fromtimestamp(end_time / 1000)}.csv'

with open(csv_file_name, 'w') as f:
    f.write('Open Time,Open,High,Low,Close,Volume\n')

    for year in range(start_year, datetime.now().year + 1):
        for month in range(1, 13):
            start_time = int(datetime(year, month, 1).timestamp() * 1000) 
            

            if year == datetime.now().year and month == datetime.now().month:
                end_time_month = end_time
            else:
                if month == 12:
                    end_time_month = int(datetime(year + 1, 1, 1).timestamp() * 1000)
                else:
                    end_time_month = int(datetime(year, month + 1, 1).timestamp() * 1000)
            
            print(f'get data from {datetime.fromtimestamp(start_time / 1000)} to {datetime.fromtimestamp(end_time_month / 1000)}')

            candlestick_data = fetch_candlestick_data(symbol, interval, start_time, end_time_month)
            
            for row in candlestick_data:
                f.write(f"{pd.to_datetime(row[0], unit='ms')},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n")

print(f"Candlestick data from {start_year} to now written to {csv_file_name}")
