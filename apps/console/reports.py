from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import ParagraphStyle

import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

class StudentReport():

    def __init__(self, student, points):
        self.student = student
        self.points = points

    def generate(self):

        buffer = BytesIO()
        Story=[]
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

        student = '<font size=16>{} {}: Behaviour Tracking</font>'.format(self.student.first_name, self.student.last_name)

        Story.append(Paragraph(student, styles["Center"]))
        Story.append(Spacer(1, 12))

        total = 0
        # Populate Full BT
        rows = [['Year', 'Term', "Week", 'Behaviour Target 1', 'Behaviour Target 2', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ]]
        for p in self.points:
            rows.append([p.year, p.term, p.week, p.b1, p.b2, p.monday_points, p.tuesday_points, p.wednesday_points, p.thursday_points, p.friday_points])
            total += (p.monday_points + p.tuesday_points + p.wednesday_points + p.thursday_points + p.friday_points)

        table = Table(rows)
        table.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.25, colors.gray)]))
        Story.append(table)



        p = Paragraph("<font size=12>Average Points: {}</font>".format(total/(len(self.points) * 5)), styles['Justify'])
        Story.append(p)
        doc.build(Story)
        pdf = buffer.getvalue()
        buffer.close()

        return pdf
