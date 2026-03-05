from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from src.models import SimRun, Result

class PDFExporter:
    def __init__(self):
        pass

    def export(self, run_id):
        # Get results from DB
        run = SimRun.get_by_id(run_id)
        results = Result.get_by_run_id(run_id)
        
        # Create PDF document
        doc = SimpleDocTemplate(f"report_{run_id}.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Add title
        title = Paragraph("Supply Chain Risk Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Add summary
        summary = Paragraph(f"Scenario: {run.scenario_id}", styles['Normal'])
        story.append(summary)
        story.append(Spacer(1, 12))
        
        # Add results table
        data = [
            ["Metric", "P50", "P90", "P99"],
            ["Revenue at Risk", f"${results['revenue_at_risk']['p50']}", f"${results['revenue_at_risk']['p90']}", f"${results['revenue_at_risk']['p99']}"]
        ]
        
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'black'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), '#FFFFFF'),
            ('GRID', (0, 0), (-1, -1), 1, 'black')
        ]))
        
        story.append(table)
        doc.build(story)
        return f"report_{run_id}.pdf"
