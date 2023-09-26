import os
import shutil
import math

# Define the source folder and destination folder prefix
source_folder = os.path.expanduser("~/Desktop/<source-folder>")
destination_folder_prefix = os.path.expanduser("~/Desktop/<destination-folder>")


# Function to calculate folder size
def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


# Create a destination folder if it doesn't exist
if not os.path.exists(destination_folder_prefix):
    os.makedirs(destination_folder_prefix)

# Initialize variables
current_folder_index = 1
current_destination_folder = f"{destination_folder_prefix}{current_folder_index}"

# Iterate through files in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_filepath = os.path.join(root, file)

        # Check if the current destination folder exceeds 1 GB
        while os.path.exists(current_destination_folder) and get_folder_size(current_destination_folder) >= 1e9:
            current_folder_index += 1
            current_destination_folder = f"{destination_folder_prefix}{current_folder_index}"

        # Create a new destination folder if it doesn't exist
        if not os.path.exists(current_destination_folder):
            os.makedirs(current_destination_folder)

        # Copy the file to the current destination folder
        shutil.copy(source_filepath, current_destination_folder)
        print(f"Copied '{file}' to '{current_destination_folder}'")

print("Separation into 1 GB folders complete.")
