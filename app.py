from flask import Flask, jsonify

app = Flask(__name__)

# Default route for the root ("/") to avoid 404 errors
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the FUNN Fuel Prices API!", "endpoints": ["/fuel-prices"]})

# Main fuel price endpoint
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
    app.run(host="0.0.0.0", port=5000)
