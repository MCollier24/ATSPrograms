import os

from tkinter.filedialog import askdirectory

def main():
    directory = askdirectory(title = "Select Saved File Directory")
    
    txtPUNs = []
    pngPUNs = []
    jpgPUNs = []
    
    #Loop through files in chosen directory and delete duplicate PUN numbers
    for filename in os.listdir(directory):
        
        #If its a failed image check if its a duplicate PUN and delte if so
        if get_status(filename) == "Fail":
            current_PUN = get_PUN(filename)
            if filename.endswith(".txt"):
                if current_PUN in txtPUNs:
                    os.remove(directory + "/" + filename)
                    print("Duplicate TXT PUN (" + current_PUN + ") Removed!")
                else:
                    txtPUNs.append(current_PUN)
            elif filename.endswith(".png"):
                if current_PUN in pngPUNs:
                    os.remove(directory + "/" + filename)
                    print("Duplicate PNG PUN (" + current_PUN + ") Removed!")
                else:
                    pngPUNs.append(current_PUN)
            elif filename.endswith(".jpg"):
                if current_PUN in jpgPUNs:
                    os.remove(directory + "/" + filename)
                    print("Duplicate JPG PUN (" + current_PUN + ") Removed!")
                else:
                    jpgPUNs.append(current_PUN)
            else:
                print("Invalid File Type")
                continue

get_PUN = lambda filename: filename.split("-")[2]

get_status = lambda filename: filename.split("-")[3]

if __name__ == "__main__":
    main()