#coding=windows-1251
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def convert_docx_to_pdf(docx_filename, pdf_filename):
    # ��������� .docx ����
    doc = Document(docx_filename)
    # ������� PDF � ������� ReportLab
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    text_object = c.beginText(72, letter[1] - 72) # �������� � �������� ������ ����

    for para in doc.paragraphs:
        # ������������ ����� � �������� ���������
        text_object.textLine(para.text.encode('utf-8')) # ��������� ����� � PDF

    c.drawText(text_object)
    c.save() # ��������� PDF

    # ���������� ������ �� BytesIO � ����
    with open(pdf_filename, 'wb') as f:
        f.write(packet.getvalue())

# ������������� �������
convert_docx_to_pdf('� ���.docx', 'asd.pdf')