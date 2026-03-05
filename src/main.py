from fastapi import FastAPI, UploadFile, File, HTTPException
from src.routes.supply_chain import supply_chain_router
from src.routes.reports import reports_router
from celery import Celery
import os

app = FastAPI(title="AI Supply Chain Stress Tester")

# Celery setup
app.celery_app = Celery(
    "supplychain_simulator",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:63779/0")
)

# Include routers
app.include_router(supply_chain_router, prefix="/api/supply-chain", tags=["supply_chain"])
app.include_router(reports_router, prefix="/api/report", tags=["reports"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "workers": 10, "queue_depth": 0}
