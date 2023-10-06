import os
import shutil

source_dir = input("Enter path of source directory: ")
destination_dir = input("Enter path of target directory: ") 

# Get the list of all files and directories in the source directory
files = os.listdir(source_dir)

for file in files:
    # Specify the full path of each file
    file_path = os.path.join(source_dir, file)

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        # Determine the destination path based on sorting criteria
        destination_path = os.path.join(destination_dir, file)

        # Copy the file to the destination directory
        shutil.copy(file_path, destination_path)

# Cross-check that all files have been copied succesfully
source_files = os.listdir(source_dir)
destination_files = os.listdir(destination_dir)

if len(source_files) == len(destination_files):
    print("All files copied successfully!")
    # Optionally, you can now delete the files in the source directory
    for file in source_files:
        file_path = os.path.join(source_dir, file)
        os.remove(file_path)
    print("Files in the source directory have been removed.")
else:
    print("an error occured during the file copying process. Please check the source and destination directories.")
    