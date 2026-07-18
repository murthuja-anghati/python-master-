import pandas as pd 
import csv
import csv

def readCSVWithModule(filePath: str) -> None:
    with open(filePath, "r") as f:
        # csv.reader automatically parses commas and handles quotes perfectly
        reader = csv.reader(f)
        for row in reader:
            print(row)

def readCSV(filePath: str)->None:
    with open(filePath ,"r") as f:
        for line in f:
            print(line.strip().upper())            

#readCSVWithModule("Flight_data_1.csv")
#readCSV("Flight_data_1.csv")

def cleanEachRow(filePath: str)->list:
    cleandRows = []
    with open(filePath,"r") as f:
        for line in f:
            parts = line.strip().split(",")
            cleand = [p.strip().lower() for p in parts]
            cleandRows.append(cleand)
    return cleandRows     
    

cleanEachRow =     cleanEachRow("Flight_data_1.csv")
print(cleanEachRow)

def readFileXlsx(filePath: str)->None:
    df = pd.read_excel(filePath)
    print(df)

#readFileXlsx("Flight_data.xlsx")  

def writeCSV(filePath: str) -> list:
    cleaned_rows = []

    # Step 1: Read the original CSV
    with open(filePath, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            cleaned = [p.strip().lower() for p in parts]
            cleaned_rows.append(cleaned)

    # Step 2: Write cleaned rows to a new file
    with open("clean_" + filePath, "w") as f:
        for row in cleaned_rows:
            f.write(",".join(row) + "\n")

    return cleaned_rows


writeCSV("Flight_data_1.csv")


#writeCSV("Flight_data_1.csv")
#WriteCSV("Flight_data_1.csv")

    
def handlingMissedRecords(filePath:str) ->None:
    cleanedRows= []
    with open(filePath,"r") as f:
        for line in f:
            if line == "":
                continue
            cleanEachRow.append(line.strip())
def handlingMissedValues(filePath:str) ->None:
    cleanedRows =[]
    with open(filePath,"r") as f:
        for line in f:
            parts = line.split(",") 
            parts = ["NA" if p == "" else p for p in parts ]
            cleanedRows.append(parts)

#start reading with ope(filename,r) ->non,list:
#start loop 
#clean with strip 
#assign to new cleaned and split with ","
#apply ur business logic on each element 
#assign this final to cleaned 
#apped this to main variable.
