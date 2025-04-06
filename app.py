from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

# Stock symbol
STOCK_SYMBOL = "AAPL"

@app.route("/stock", methods=["GET"])
def get_stock_data():
    try:
        stock = yf.Ticker(STOCK_SYMBOL)
        data = stock.history(period="1d")
        current_price = data["Close"].iloc[-1]
        return jsonify({"symbol": STOCK_SYMBOL, "current_price": current_price})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/stock/info", methods=["GET"])
def get_stock_info():
    try:
        stock = yf.Ticker(STOCK_SYMBOL)
        info = stock.info
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
