import os
from flask import Flask, jsonify

app = Flask(__name__)

# Use the Render-assigned port (default to 5000 if not found)
PORT = int(os.getenv("PORT", 5000))

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the FUNN Fuel Prices API!", "endpoints": ["/fuel-prices"]})

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
    app.run(host="0.0.0.0", port=PORT)
