from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json

class PDFExporter:
    def export_to_pdf(self, narrative):
        doc = SimpleDocTemplate("report.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        title = Paragraph("Supply Chain Risk Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 12))

        # Add narrative content
        for key, value in narrative.items():
            if isinstance(value, list):
                story.append(Paragraph(f"{key}:", styles['Heading2']))
                for item in value:
                    story.append(Paragraph(str(item), styles['Normal']))
            else:
                story.append(Paragraph(f"{key}: {value}", styles['Normal']))

        doc.build(story)
        return "report.pdf"
