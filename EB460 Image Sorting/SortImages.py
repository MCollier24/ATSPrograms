import os
import shutil

def main():
    current_dir = os.getcwd() #This stores the directory where the code is run from

    #Loop through the png image files in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith(".png"):
            elements = filename.split("-")
            
            #Get and store the camera name from the image filename
            match elements[0]:
                case "EB460CAM1":
                    camera = "CAM1"
                case "EB460CAM2":
                    camera = "CAM2"
                case "EB460CAM3":
                    camera = "CAM3"
                case "EB460CAM4":
                    camera = "CAM4"
                case other:
                    continue
            
            #Get and store the recipe value from the image filename
            match elements[1][0]:
                case "1":
                    recipe = "Recipe 1"
                case "2":
                    recipe = "Recipe 2"
                case "3":
                    recipe = "Recipe 3"
                case other:
                    continue
            
            #Get and store the shot number from teh image filename
            match elements[1][1]:
                case "1":
                    task = "Task 1"
                case "2":
                    task = "Task 2"
                case "3":
                    task = "Task 3"
                case "4":
                    task = "Task 4"
                case other:
                    continue
            
            #Move the image to the correct directory
            try:
                #os.rename(current_dir + "\\" + filename, current_dir + "\\" + camera + "\\" + recipe + "\\" + task + "\\" + filename)
                shutil.move(current_dir + "\\" + filename, current_dir + "\\" + camera + "\\" + recipe + "\\" + task + "\\" + filename)
            except FileExistsError:
                os.remove(current_dir + "\\" + filename)
                continue

if __name__ == "__main__":
    main()