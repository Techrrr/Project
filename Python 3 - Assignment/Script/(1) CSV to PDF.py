import pdfkit
import pandas as pd

# CSV to HTML
# Input FIle
CSV = pd.read_csv(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Input\names.csv")  
CSV.to_html(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names.html")  

# HTML to PDF
# Output FIle
pdfkit.from_file(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names.html" , r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names.pdf")