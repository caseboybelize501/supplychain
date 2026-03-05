from fastapi import FastAPI, UploadFile, File, HTTPException
from celery.result import AsyncResult
from src.routes.supply_chain import router as supply_chain_router
from src.routes.reports import router as reports_router
from src.workers.sim_worker import celery_app
import os

class Settings:
    database_url = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/db")
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

app = FastAPI(title="AI Supply Chain Stress Tester")

app.include_router(supply_chain_router)
app.include_router(reports_router)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "workers": len(celery_app.control.inspect().active() or {}),
        "redis_queue_depth": celery_app.control.inspect().active_queues()
    }
