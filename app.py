import os
from flask import Flask, jsonify

app = Flask(__name__)

# Use Render-assigned port or default to 5000
PORT = int(os.getenv("PORT", 5000))

# Allow all origins (CORS support) to prevent access restrictions
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the FUNN Fuel Prices API!",
        "endpoints": ["/fuel-prices"]
    })

@app.route("/fuel-prices", methods=["GET"])
def get_fuel_prices():
    data = {
        "facts": [
            {
                "Month/Year": "MAR25",
                "Day": "10MAR25",
                "Product group": "Road transport diesel",
                "Product": "Road Diesel B7 (€/L)",
                "Price incl. VAT": 1.4044044044044
            }
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    print(f"🚀 Running on port {PORT}")
    app.run(host="0.0.0.0", port=PORT)
