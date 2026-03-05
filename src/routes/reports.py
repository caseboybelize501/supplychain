from fastapi import APIRouter, HTTPException
from src.models import SimRun, Result
from src.synthesis.risk_narrator import RiskNarrator
from src.exporters.pdf_exporter import PDFExporter
import json

reports_router = APIRouter()

@reports_router.get("/{job_id}")
def get_simulation_results(job_id: str):
    try:
        run = SimRun.get_by_id(job_id)
        results = Result.get_by_run_id(job_id)
        return {
            "run": run,
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@reports_router.get("/{id}/report")
def generate_risk_report(id: str):
    try:
        run = SimRun.get_by_id(id)
        results = Result.get_by_run_id(id)
        narrator = RiskNarrator()
        narrative = narrator.generate_narrative(run, results)
        return narrative
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@reports_router.post("/{id}/export")
def export_to_pdf(id: str):
    try:
        exporter = PDFExporter()
        pdf_path = exporter.export(id)
        return {"pdf_path": pdf_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
