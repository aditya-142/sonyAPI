from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Sony India AI Agent Demo")

# -------------------- MODELS --------------------
class DemandForecast(BaseModel):
    product: str
    region: str
    month: str
    forecast_units: int

class LogisticsRoute(BaseModel):
    origin: str
    destination: str
    distance_km: int
    delay_minutes: int

class SupplierRisk(BaseModel):
    supplier_id: str
    name: str
    region: str
    on_time_pct: float
    defect_rate: float
    financial_score: int

class Inventory(BaseModel):
    product_id: str
    warehouse: str
    stock: int
    reorder_point: int
    max_capacity: int

class QualityReport(BaseModel):
    batch_id: str
    product_id: str
    units_tested: int
    defects_found: int

class Recommendation(BaseModel):
    user_id: str
    preferences: List[str]
    recent_views: List[str]

class Pricing(BaseModel):
    product_id: str
    base_price: int
    demand_level: str
    competitor_price: int

class Query(BaseModel):
    user_id: str
    query: str

class Fraud(BaseModel):
    transaction_id: str
    user_id: str
    flagged_reason: str

class Vendor(BaseModel):
    vendor_id: str
    name: str
    rating: float
    cost_efficiency: float

class Contract(BaseModel):
    contract_id: str
    vendor_id: str
    risk_flags: List[str]
    expiry_date: str

class PurchaseOrder(BaseModel):
    po_id: str
    item: str
    quantity: int
    vendor_id: str
    status: str

class SalesAnalytics(BaseModel):
    region: str
    product: str
    units_sold: int
    month: str

class CustomerBehavior(BaseModel):
    user_id: str
    clicks: int
    time_on_site: float
    conversions: int

class Trend(BaseModel):
    keyword: str
    mentions: int
    sentiment: str

class Maintenance(BaseModel):
    device_id: str
    issue: str
    predicted_failure_date: str

class KPI(BaseModel):
    metric: str
    value: float
    target: float

class DeviceStatus(BaseModel):
    device_id: str
    status: str
    last_check: datetime

# -------------------- STORAGE --------------------
db = {
    "demand": [],
    "logistics": [],
    "supplier": [],
    "inventory": [],
    "quality": [],
    "recommendations": [],
    "pricing": [],
    "queries": [],
    "fraud": [],
    "vendors": [],
    "contracts": [],
    "purchase_orders": [],
    "sales": [],
    "behavior": [],
    "trends": [],
    "maintenance": [],
    "kpis": [],
    "devices": [],
}

# -------------------- ROUTES --------------------
@app.get("/")
def root():
    return {"message": "Sony India AI Agent is running."}

# Supply Chain
@app.post("/supplychain/demand")
def add_demand(item: DemandForecast): db["demand"].append(item); return {"added": True}

@app.get("/supplychain/demand")
def get_demand(): return db["demand"]

@app.post("/supplychain/logistics")
def add_logistics(item: LogisticsRoute): db["logistics"].append(item); return {"added": True}

@app.get("/supplychain/logistics")
def get_logistics(): return db["logistics"]

@app.post("/supplychain/supplier")
def add_supplier(item: SupplierRisk): db["supplier"].append(item); return {"added": True}

@app.get("/supplychain/supplier")
def get_suppliers(): return db["supplier"]

@app.post("/supplychain/inventory")
def add_inventory(item: Inventory): db["inventory"].append(item); return {"added": True}

@app.get("/supplychain/inventory")
def get_inventory(): return db["inventory"]

@app.post("/supplychain/quality")
def add_quality(item: QualityReport): db["quality"].append(item); return {"added": True}

@app.get("/supplychain/quality")
def get_quality(): return db["quality"]

# Ecommerce
@app.post("/ecommerce/recommendations")
def add_reco(item: Recommendation): db["recommendations"].append(item); return {"added": True}

@app.get("/ecommerce/recommendations")
def get_reco(): return db["recommendations"]

@app.post("/ecommerce/pricing")
def add_price(item: Pricing): db["pricing"].append(item); return {"added": True}

@app.get("/ecommerce/pricing")
def get_price(): return db["pricing"]

@app.post("/ecommerce/queries")
def add_query(item: Query): db["queries"].append(item); return {"added": True}

@app.get("/ecommerce/queries")
def get_queries(): return db["queries"]

@app.post("/ecommerce/fraud")
def add_fraud(item: Fraud): db["fraud"].append(item); return {"added": True}

@app.get("/ecommerce/fraud")
def get_fraud(): return db["fraud"]

# Procurement
@app.post("/procurement/vendors")
def add_vendor(item: Vendor): db["vendors"].append(item); return {"added": True}

@app.get("/procurement/vendors")
def get_vendors(): return db["vendors"]

@app.post("/procurement/contracts")
def add_contract(item: Contract): db["contracts"].append(item); return {"added": True}

@app.get("/procurement/contracts")
def get_contracts(): return db["contracts"]

@app.post("/procurement/purchase_orders")
def add_po(item: PurchaseOrder): db["purchase_orders"].append(item); return {"added": True}

@app.get("/procurement/purchase_orders")
def get_po(): return db["purchase_orders"]

# Analytics
@app.post("/analytics/sales")
def add_sales(item: SalesAnalytics): db["sales"].append(item); return {"added": True}

@app.get("/analytics/sales")
def get_sales(): return db["sales"]

@app.post("/analytics/behavior")
def add_behavior(item: CustomerBehavior): db["behavior"].append(item); return {"added": True}

@app.get("/analytics/behavior")
def get_behavior(): return db["behavior"]

@app.post("/analytics/trends")
def add_trend(item: Trend): db["trends"].append(item); return {"added": True}

@app.get("/analytics/trends")
def get_trends(): return db["trends"]

@app.post("/analytics/maintenance")
def add_maint(item: Maintenance): db["maintenance"].append(item); return {"added": True}

@app.get("/analytics/maintenance")
def get_maint(): return db["maintenance"]

# Dashboard
@app.post("/dashboard/kpis")
def add_kpi(item: KPI): db["kpis"].append(item); return {"added": True}

@app.get("/dashboard/kpis")
def get_kpis(): return db["kpis"]

@app.post("/dashboard/devices")
def add_device(item: DeviceStatus): db["devices"].append(item); return {"added": True}

@app.get("/dashboard/devices")
def get_devices(): return db["devices"]
