import os
import shutil

# Replace with your source directory path
source_directory = 'sign_data\\train'

# Replace with your destination directory path
destination_directory = 'clean_sign_dataset'

# Create destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Walk through all subdirectories and files in the source directory
for root, dirs, files in os.walk(source_directory):
    for dir in dirs:
        if 'forg' in dir:
            continue
        for root_, dirs_, files_ in os.walk(os.path.join(source_directory, dir)):
            for file in files_:
                # Construct full file path
                file_path = os.path.join(root, dir, file)
                # Construct destination file path
                destination_path = os.path.join(destination_directory, file)
                # Move the file
                shutil.copy(file_path, destination_path)