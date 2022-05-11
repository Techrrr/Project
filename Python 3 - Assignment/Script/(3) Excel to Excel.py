import pandas as pd

# Excel to Excel
ExcelFile = pd.read_excel(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Input\names.xlsx")
ExcelFile.to_excel(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names_xlsx.xlsx")