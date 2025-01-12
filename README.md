# Get Cryptocurrency Data from Binance

This project fetches historical candlestick data for Cryptocurrency (like BTC) from the Binance API and saves it to a CSV file. The data can be used for analysis, backtesting trading strategies, or any other purpose that requires historical price information.

## Features

- Fetches candlestick data for Cryptocurrency over a customizable date range.
- Writes the data directly to a CSV file to minimize memory usage.
- Handles pagination to ensure all available data is retrieved.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yuzaiakira/binance-python-candle-fetcher.git
   cd binance-python-candle-fetcher
   ```

2. Install the required libraries:

    ``` bash
    pip install requests pandas
    ```

## Usage

1. Open the `get_price.py` file in your preferred code editor.
   
2.  Modify the following variables to suit your needs:
   - **symbol**: Change this to the cryptocurrency symbol you want to fetch data for (e.g., 'BTCUSDT' for Bitcoin).
   - **interval**: Set this to the desired candlestick interval (e.g., '15m' for 15 minutes).
   - **start_year**: Update this to the year from which you want to start fetching historical data (e.g., 2017).

3. After making your changes, save the file and run the script to fetch the data:

    ```bash
    python get_price.py
    ```
4. The script will create a CSV file named `{symbol}_15m_data_{start_year}_{end_time}.csv` in the same directory, containing the historical candlestick data.

## TODO
- [ ] Set Up Command-Line Interface
- [ ] Make as linux Command
- [ ] Modify Documentation
- [ ] Write Test 😭