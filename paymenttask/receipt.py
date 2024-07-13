from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

def create_receipt(file_name):
    # Create document
    pdf = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='Title', fontName='Helvetica-Bold', fontSize=18, alignment=1, spaceAfter=20)
    normal_style = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, spaceAfter=12)
    bold_style = ParagraphStyle(name='Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', spaceAfter=12)

    # Title
    title = Paragraph("Payment Receipt", title_style)
    elements.append(title)

    # Information Table
    info_data = [
        ["Date:", "2024-07-10"],
        ["Receipt No:", "12345"],
        ["Customer Name:", "John Doe"],
        ["Customer Email:", "john.doe@example.com"]
    ]
    info_table = Table(info_data, colWidths=[100, 200])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(info_table)

    # Spacer
    elements.append(Spacer(1, 12))

    # Transaction Table
    transaction_data = [
        ["Item", "Description", "Quantity", "Price", "Total"],
        ["Item 1", "Product 1 Description", "2", "$10", "$20"],
        ["Item 2", "Product 2 Description", "1", "$15", "$15"],
        ["Item 3", "Product 3 Description", "5", "$7", "$35"],
    ]
    transaction_table = Table(transaction_data, colWidths=[50, 200, 50, 50, 50])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(transaction_table)

    # Spacer
    elements.append(Spacer(1, 12))

    # Total Amount
    total_amount = Paragraph("Total Amount: $70", bold_style)
    elements.append(total_amount)

    # Spacer
    elements.append(Spacer(1, 24))

    # Proceed to Checkout
    checkout_paragraph = Paragraph(
        '<font color="white">PROCEED TO CHECKOUT</font>',
        ParagraphStyle(
            name="ProceedButton",
            backColor=colors.red,
            alignment=1,
            padding=10,
            borderPadding=5,
        ),
    )
    elements.append(checkout_paragraph)

    # Build PDF
    pdf.build(elements)

# Create receipt
create_receipt("payment_receipt.pdf")
