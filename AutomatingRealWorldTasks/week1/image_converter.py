#!/usr/bin/python3
from PIL import Image
import glob

for file in list(glob.glob('*dp')):
  im = Image.open(file)
  new_im = im.resize((128,128)).rotate(90).convert('RGB')
  new_im.save(r"/opt/icons/" + str(file) + ".jpg")

#img = Image.open("/opt/icons/ic_edit_location_black_48dp.jpg")
#print("{}, {}".format(img.format, img.size))
