#!/usr/bin/env python3
"""This script can only work if a folder named 'images' is located in the same
directory as the script with image files of '.png' type.

a new folder named 'new_images will ge created to store the processed images.

The type of file to be processed and after processing can be changed by
changing the extensions.
"""

import subprocess
import os

from PIL import Image

# create a list of image files to be processed
directory = os.path.join(os.getcwd(), 'images')  # cwd + 'images'
print("Directory for getting images to be processed: ", directory)

png_files = [files for files in os.listdir(directory) if os.path.splitext(files)[1]
        == '.png']
# To change the type of files to be processed, change the extension in above line
processed_images = []  # List of processed image files

# Create new folder to store processed image files
try:
    subprocess.run(['mkdir', 'new_images'])
except:
    print("Directory named 'new_images' already exists.\n")

# Path to new_images directory
new_image_dir = os.path.join(os.getcwd(), 'new_images')
print("New directory to store processed files: ", new_image_dir)
print()
print("[Processing image files]\n")
# Loop over the list of images to be processed and process as per requirement
for image_file in png_files:

    image_path = os.path.join(directory, str(image_file))
    print("Image file original path: ", image_path)

    # Split filename and extension from basename
    base = os.path.basename(image_path)
    # Get basename of file to join to new path 
    filename = os.path.splitext(base)[0]

    out_filename = filename + '.jpeg'  # change extension
    # To change the extension of output file, change the extension in above line
    # For example you can change from '.jpeg' to '.png' if required
    print("Name of processed image file: ", out_filename)
    output_path = os.path.join(new_image_dir, str(out_filename))
    print("Path of processed image file: ", output_path)
    print()

    # Open original image file as object, process and save 
    image_obj = Image.open(image_path)
    try:
        image_obj.rotate(90).resize((256, 256)).convert("RGB").save(output_path)
        processed_images.append(output_path)
    except:
        print("Not able to convert file: ", image_file)

# List all the processed images
print()
print("List of processed files\n")
for images in processed_images:
    print(images)
