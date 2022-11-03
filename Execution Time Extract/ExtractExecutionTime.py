import os
import csv

from glob import iglob
from tkinter.filedialog import askdirectory

def main():
    directory = askdirectory(title = "Select Directory")
    print("Getting execution time from text files in: " + directory)
    
    try:
        with open('ExecutionTimes.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, dialect='excel')    #Create csv writer object
            csv_writer.writerow(["PUN", "Status", "Recipe/Task", "Total Execution Time (s)"])   #Write the header into the csv file
            
            #Loop through files in chosen directory and write data to csv file
            for filename in iglob(directory + "/**", recursive=True):
                if filename.endswith('.txt'):
                    try:
                        with open (filename, 'r') as file:
                            execution_time = ''
                            for i, line in enumerate(file):
                                match i:
                                    #If the line number is 303 (where the execution time data is) store the info
                                    case 303:
                                        execution_time = line.rstrip()[22::]                          
                                    case _:
                                        continue
                            
                            csv_writer.writerow([get_PUN(filename), get_status(filename), get_shot(filename), execution_time])
                    except  FileNotFoundError:
                        continue
            
            print("Process Complete!")
    except PermissionError:
        print("[ERROR] - Please close the .csv file before running this program!")

get_shot = lambda filename: filename.split("\\")[-1].split("-")[1]

get_PUN = lambda filename: filename.split("\\")[-1].split("-")[2]

get_status = lambda filename: filename.split("\\")[-1].split("-")[3]

if __name__ == "__main__":
    main()