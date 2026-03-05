from fastapi import APIRouter, HTTPException
from src.models import SimRun, Result
from src.synthesis.risk_narrator import RiskNarrator
from src.exporters.pdf_exporter import PDFExporter
import json

router = APIRouter(prefix="/report", tags=["Reports"])

@router.get("/{id}/export")
def export_report(id: str):
    try:
        # Fetch simulation results
        run = SimRun.objects.get(id=id)
        result = Result.objects.get(sim_run=run)

        # Generate narrative
        narrator = RiskNarrator()
        narrative = narrator.generate_narrative(run, result)

        # Export to PDF
        exporter = PDFExporter()
        pdf_path = exporter.export_to_pdf(narrative)
        return {"pdf_path": pdf_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
