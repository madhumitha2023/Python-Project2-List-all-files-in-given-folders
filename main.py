#This code is written to list all the files of the folders given as an input by the users

import os

def list_files_in_folders(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
        

def main():
    folders_path = input("Please provide the path of folders with spaces in between: ").split()
    
    for folder in folders_path:
        files, error_message = list_files_in_folders(folder)
    
        if files:
            print(f"======Below are the files under the folder {folder}=======")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder}: {error_message}")
        


if __name__ == "__main__":
    main()
        
        