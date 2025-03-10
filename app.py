from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/fuel-prices', methods=['GET'])
def get_fuel_prices():
    latest_date, latest_data = fetch_latest_fuel_prices()
    
    # Format date for metadata
    updated_date = datetime.strptime(latest_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    
    # Construct metadata
    metadata = {
        "id": "unique-dataset-id",
        "label": "Fuel Prices",
        "description": "Daily fuel prices at Juodeikiai station.",
        "updated": updated_date
    }
    
    # Construct facts
    facts = []
    for entry in latest_data:
        date_obj = datetime.strptime(entry['Date'], "%Y-%m-%d")
        fact = {
            "Month/Year": date_obj.strftime("%b%y").upper(),
            "Day": date_obj.strftime("%d%b%y").upper(),
            "Product group": determine_product_group(entry['Product']),
            "Product": f"{entry['Product']} (€/L)",
            "Price incl. VAT": entry['Price']
        }
        facts.append(fact)
    
    # Combine metadata and facts
    response = {
        "metadata": metadata,
        "facts": facts
    }
    
    return jsonify(response)

def determine_product_group(product_name):
    # Logic to determine product group based on product name
    if "diesel" in product_name.lower():
        return "Road transport diesel"
    elif "petrol" in product_name.lower() or "gasoline" in product_name.lower():
        return "Petrol"
    else:
        return "Other"
