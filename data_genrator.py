import requests

base = "http://127.0.0.1:8000"

def post(endpoint, payloads):
    for p in payloads:
        res = requests.post(f"{base}{endpoint}", json=p)
        print(f"{endpoint} =>", res.status_code)

# --- Supply Chain: Demand Forecast ---
post("/supplychain/demand", [
    {"product": "Bravia OLED TV", "region": "North", "month": "July", "forecast_units": 5200},
    {"product": "Alpha Mirrorless Camera", "region": "South", "month": "August", "forecast_units": 3100},
    {"product": "Sony WH-1000XM5", "region": "West", "month": "September", "forecast_units": 6800},
    {"product": "HT-A7000 Soundbar", "region": "East", "month": "October", "forecast_units": 3900},
    {"product": "PlayStation 5", "region": "North", "month": "November", "forecast_units": 7500}
])

# --- Logistics ---
post("/supplychain/logistics", [
    {"origin": "Sony Warehouse - Delhi", "destination": "Sony Retail - Mumbai", "distance_km": 1450, "delay_minutes": 35},
    {"origin": "Sony Hub - Chennai", "destination": "Sony Showroom - Bangalore", "distance_km": 340, "delay_minutes": 12}
])

# --- Supplier Risk ---
post("/supplychain/supplier", [
    {"supplier_id": "SNY01", "name": "Rico Electronics", "region": "Maharashtra", "on_time_pct": 97.5, "defect_rate": 0.5, "financial_score": 90}
])

# --- Inventory ---
post("/supplychain/inventory", [
    {"product_id": "BRV-55A80K", "warehouse": "Mumbai", "stock": 140, "reorder_point": 90, "max_capacity": 300},
    {"product_id": "PS5-STD", "warehouse": "Delhi", "stock": 85, "reorder_point": 60, "max_capacity": 180}
])

# --- Quality Report ---
post("/supplychain/quality", [
    {"batch_id": "QA202407", "product_id": "BRV-55A80K", "units_tested": 100, "defects_found": 1}
])

# --- Ecommerce: Recommendations ---
post("/ecommerce/recommendations", [
    {"user_id": "USR1001", "preferences": ["PlayStation", "Soundbar"], "recent_views": ["PS5-STD", "HT-A7000"]}
])

# --- Ecommerce: Pricing ---
post("/ecommerce/pricing", [
    {"product_id": "WH-1000XM5", "base_price": 29990, "demand_level": "High", "competitor_price": 28990}
])

# --- Ecommerce: Queries ---
post("/ecommerce/queries", [
    {"user_id": "USR1002", "query": "Is there cashback on Bravia OLED TV?"}
])

# --- Ecommerce: Fraud ---
post("/ecommerce/fraud", [
    {"transaction_id": "TXN-0001", "user_id": "USR1001", "flagged_reason": "Suspicious login from overseas"}
])

# --- Procurement: Vendors & Contracts ---
post("/procurement/vendors", [
    {"vendor_id": "VNDR-SNY", "name": "Sony Approved Vendor Co.", "rating": 4.7, "cost_efficiency": 93.2}
])

post("/procurement/contracts", [
    {"contract_id": "SNY-CON-2024", "vendor_id": "VNDR-SNY", "risk_flags": ["Late Delivery in FY23"], "expiry_date": "2027-03-31"}
])

post("/procurement/purchase_orders", [
    {"po_id": "PO-SNY-101", "item": "HT-A7000", "quantity": 200, "vendor_id": "VNDR-SNY", "status": "Approved"}
])

# --- Analytics ---
post("/analytics/sales", [
    {"region": "South", "product": "Sony WH-1000XM5", "units_sold": 1600, "month": "June"}
])

post("/analytics/behavior", [
    {"user_id": "USR1001", "clicks": 24, "time_on_site": 420.0, "conversions": 1}
])

post("/analytics/trends", [
    {"keyword": "Sony Alpha Camera", "mentions": 12000, "sentiment": "Positive"}
])

post("/analytics/maintenance", [
    {"device_id": "BRV-55A80K", "issue": "Panel flickering", "predicted_failure_date": "2025-08-15"}
])

# --- Dashboard ---
post("/dashboard/kpis", [
    {"metric": "PS5 Sales Growth", "value": 12.5, "target": 10.0}
])

post("/dashboard/devices", [
    {"device_id": "PS5-STD", "status": "Active", "last_check": "2025-07-11T10:00:00"}
])
