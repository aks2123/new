from PIL import Image
import os.path, sys

path = "imgs"
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((90,55,450,450)) #corrected lower the 2nd value for crop from top
            imResize = imCrop.resize((512,512), Image.ANTIALIAS)
            imResize.save(f + 'Cropped.jpg', "JPEG", dpi=(96,96) )

crop()
