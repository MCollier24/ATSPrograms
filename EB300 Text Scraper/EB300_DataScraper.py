#EB300 - Data Scraping
import os
import csv

from tkinter.filedialog import askdirectory

directory = askdirectory(initialdir = '/',title = "Select Tab Data Directory:")

#Open CSV file to write tab data to
if not directory == False:
    with open(os.getcwd() + "\\EB300TabLengthData.csv", "w", newline='') as dataFile:
        print("Parsing Files")
        dataWriter = csv.writer(dataFile, dialect='excel')
        #Setup header in csv file
        dataWriter.writerow(["PUN","Task ID","Datum Length","Datum Angle","Non-Datum Length","Non-Datum Angle"])
        #Loop through the tab length data files
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith("EB300TabLengthData"):
                with open(directory + "\\" + filename, "r") as f:
                    #Loop through each line in the file
                    while (line := f.readline().rstrip()):
                        elements = line.split("_")
                        if elements[2] == "Pass":
                            dataWriter.writerow([elements[1].strip(),elements[3],elements[5],elements[7],elements[6],elements[8].rstrip()])
                        continue    
                continue
            else:
                continue
else:
    print("No Files in Directory")