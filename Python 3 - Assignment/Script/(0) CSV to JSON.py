import csv,json

#File names to import/export - Reads the file
csvFilePath = (r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Input\names.csv")
jsonFilePath = (r"C:\Users\Administrator\Documents\Work\Python 3 - Assignment\Output\names.json")

#Organising the CSV file - Creates an Object
data={}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        name = csvRow["name"]
        data[name] =csvRow

#Converting & Exporting to JSON format.
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data))