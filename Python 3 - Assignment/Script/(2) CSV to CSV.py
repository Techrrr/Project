import pandas as pd

# CSV to CSV
csvFile = pd.read_csv(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Input\names.csv")
csvFile.to_csv(r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names_csv.csv")