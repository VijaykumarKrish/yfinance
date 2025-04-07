import yfinance as yf
import json

# List of stock ticker symbols

def fetch_stock_data(tickers):
    stock_data = {}
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        #data = stock.history(period='1d', interval='1m')  # Fetching 1 day of data at 1-minute intervals
        info = stock.info
        # Convert the DataFrame to a dictionary
        #stock_data[ticker] = data.reset_index().to_dict(orient='records')  # Convert to list of dictionaries
        stock_data[ticker] = {
            "current_price": info.get("currentPrice"),
            "previous_close": info.get("regularMarketPreviousClose"),
            "open": info.get("regularMarketOpen"),
            "high": info.get("dayHigh"),
            "low": info.get("dayLow"),
            "volume": info.get("volume"),
            "market_cap": info.get("marketCap"),
            "dividend_yield": info.get("dividendYield"),
        }
    
    return stock_data
