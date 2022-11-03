import os
import csv

from tkinter.filedialog import askdirectory

def main():
    directory = askdirectory(title = "Select Text File Directory")
    
    line_numbers = [54, 55, 56, 57, 58, 59]
    
    with open('EB300BlobAreas.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')    #Create csv writer object
        csv_writer.writerow(["PUN", "Status", "Orientation", "VC2 Blob 1","VC2 Blob 2", "VC3 Blob 1", "VC3 Blob 2"])   #Write the header into the csv file
        
        #Loop through files in chosen directory and write data to csv file
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open (directory + "\\" + filename, 'r') as file:
                    vc2_enabled = False
                    vc3_enabled = False
                    vc2_blob1 = None
                    vc2_blob2 = None
                    vc3_blob1 = None
                    vc3_blob2 = None
                    
                    for i, line in enumerate(file):
                        match i:
                            case 56:
                                if "True" in line:
                                    vc2_enabled = True
                                print(line)
                            case 57:
                                vc2_blob1 = line[26::]
                                print(line)
                            case 58:
                                vc2_blob2 = line[26::]
                                print(line)
                            case 59:
                                if "True" in line:
                                    vc3_enabled = True
                                print(line)
                            case 60:
                                vc3_blob1 = line[26::]
                                print(line)
                            case 61:
                                vc3_blob2 = line[26::]  
                                print(line)                                
                            case _:
                                continue
                    
                    if vc2_enabled and not vc3_enabled:
                        csv_writer.writerow([get_PUN(filename),get_status(filename),"TextUp",vc2_blob1,vc2_blob2,vc3_blob1,vc3_blob2])
                    elif not vc2_enabled and vc3_enabled:
                        csv_writer.writerow([get_PUN(filename),get_status(filename),"TextDown",vc2_blob1,vc2_blob2,vc3_blob1,vc3_blob2])
                    else:
                        csv_writer.writerow([get_PUN(filename),get_status(filename),"Invalid",vc2_blob1,vc2_blob2,vc3_blob1,vc3_blob2]) 

get_PUN = lambda filename: filename.split("-")[2]

get_status = lambda filename: filename.split("-")[3]

if __name__ == "__main__":
    main()