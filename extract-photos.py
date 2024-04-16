import os
import shutil

def extract_jpg(source_folder, destination_folder):
    # Recursively search for .jpg images in source folder and subfolders
    for root, dirs, files in os.walk(source_folder):
        print("sub-folder")
        for filename in files:
            if filename.endswith('.jpeg'):
                # If the file is a .jpg image, copy it to the destination folder
                source_path = os.path.join(root, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.copyfile(source_path, destination_path)

source_folder = 'C:/Users/saaniya.saraf/Documents/Normal_images'
destination_folder = 'C:/Users/saaniya.saraf/Documents/fog-image-classification/Normal'

extract_jpg(source_folder, destination_folder)