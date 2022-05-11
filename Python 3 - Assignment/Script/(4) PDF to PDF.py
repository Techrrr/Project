from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# Change the path to work on your computer if necessary
pdf_path = (
    Path.home()
    / r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names.pdf"
)
input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

with Path(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)