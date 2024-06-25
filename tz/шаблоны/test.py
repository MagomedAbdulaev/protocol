#coding=windows-1251
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def convert_docx_to_pdf(docx_filename, pdf_filename):
    # Загружаем .docx файл
    doc = Document(docx_filename)
    # Создаем PDF с помощью ReportLab
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    text_object = c.beginText(72, letter[1] - 72) # Начинаем с верхнего левого угла

    for para in doc.paragraphs:
        # Конвертируем текст в заданную кодировку
        text_object.textLine(para.text.encode('utf-8')) # Добавляем текст в PDF

    c.drawText(text_object)
    c.save() # Сохраняем PDF

    # Перемещаем данные из BytesIO в файл
    with open(pdf_filename, 'wb') as f:
        f.write(packet.getvalue())

# Использование функции
convert_docx_to_pdf('С БДД.docx', 'asd.pdf')