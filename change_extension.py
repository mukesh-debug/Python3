#!/usr/bin/env python3
import os,subprocess
from os import listdir
from os.path import isfile, join #To process filenames and extensions appropriately
from PIL import Image #Python Imaging Library to process images
"""To create a list of image files to be processed or change extension.
   use os.listdir() to list contents of a directory and then use os.path.isfile
   to select only files alternatively glob.glob could also be used here.
"""
imagefiles=[f for f in listdir('images') if isfile(join('images', f))]

try:
	subprocess.run(['mkdir', 'newimages']) #to create a new dir to store processed images
except:
	print("directory named newimages already exists in home directory")
#Process the image files to change its properties and extension to jpg
for eimage in imagefiles:
	f, e = os.path.splitext(eimage)
	outfile = f+ ".jpg"
	print("eimage:",eimage)
	imagename=os.path.join('images', str(eimage))
	print("imagename:", imagename)
	im=Image.open(imagename)
	path=str(join('newimages', outfile))
	try:
		im.rotate(90).resize((128, 128)).save(path,"JPEG")
	except:
		print("cannot convert ",imagename,"to JPEG.")
print('Printing the results of conversion, the converted files')
subprocess.run(['ls', 'newimages']) #listing processed image files on stdout
