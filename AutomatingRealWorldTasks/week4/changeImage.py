from PIL import Image
import glob

for file in list(glob.glob('/home/student-03-80cf580f56e8/supplier-data/images/*.tiff')):
  #print(file)
  im = Image.open(file)
  new_im = im.convert('RGB').resize((600,400))
  new_im.save(str(file).replace('.tiff', '.jpeg'))
