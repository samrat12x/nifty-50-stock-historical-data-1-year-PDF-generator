from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def data_2_pdf(all_data):
    pdf = SimpleDocTemplate("nifty50_dataframe.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    for stock_name, data in all_data.items():
        # Create a central header with the stock name
        title = Paragraph(stock_name, styles['Title'])
        elements.append(title)
        
        # Get the table headers
        headers = list(data.columns)
        
        # Convert the DataFrame to a list of lists, including the headers
        table_data = [headers] + [list(row) for _, row in data.iterrows()]
        
        # Create a Table object
        table = Table(table_data)
        
        # Optionally, add some style to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        
        table.setStyle(style)
        
        elements.append(table)
        elements.append(Spacer(1, 12))  # Add space between tables
    
    # Build the PDF
    pdf.build(elements)
