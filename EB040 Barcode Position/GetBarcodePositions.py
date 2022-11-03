import os
import csv
from tkinter.filedialog import askdirectory

def main():
    directory = askdirectory(title = "Select barcode reader text files") #Get directory containing the text files from the user'
    
    line_numbers = [11, 86, 89] #Store the line numbers that contain the data we need (String, X, and Y)
    
    #Create new csv file then loop through text files to extract cell X and Y position
    with open(os.getcwd() + "\\EB040BarcodePositions.csv", "w", newline='') as data_file:
        data_writer = csv.writer(data_file, dialect='excel')    #Create csv writer object
        data_writer.writerow(["Capture Time","PUN","X","Y"])   #Write the header into the csv file
        
        #Loop through text files and extract Barcode X and Y values
        for filename in os.listdir(directory):
            if filename.endswith('.txt') and "Fail" not in filename:
                with open (directory + "\\" + filename, 'r') as file:
                    timestamp = None
                    trace_code = None
                    x = None
                    y = None
                    for i, line in enumerate(file):
                        if i in line_numbers:
                            line = line.rstrip()
                            #Extract timestamp, trace code and code position from respective lines
                            if i == line_numbers[0]:
                                timestamp = line[18::]
                            elif i == line_numbers[1]:
                                trace_code = line.split("\x1d")[4][1::]
                            elif i == line_numbers[2]:
                                x = line[16:21:]
                                y = line[23:28:]
                        elif i > max(line_numbers):
                            break   #Skip lines past the highest we need data from
                        else:
                            continue
            
                    data_writer.writerow([timestamp,trace_code,x,y])  #Write new line in .csv file
    

if __name__ == "__main__":
    main()