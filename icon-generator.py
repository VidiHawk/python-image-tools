# Here are a few functions that may come handy when preparing imagery for a new website

# You will have to install PIL using sudo pip3 install python-resize-image
from xml.dom.minidom import parseString
from PIL import Image
import os, sys

# The path will need to be played around with, this code worked with my Mac
path = "/"
dirs = os.listdir(path)
pic = ""

print(dirs)


def resize_all():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            os.mkdir(f)

            # Just create 2 new lines per image size required
            imResize = im.resize((24, 24), Image.ANTIALIAS)
            imResize.save(f + "/24resized.png", "PNG", quality=100)
            imResize = im.resize((36, 36), Image.ANTIALIAS)
            imResize.save(f + "/36resized.png", "PNG", quality=100)


def generate_icons(pic):
    im = Image.open(pic)
    # Just create 2 new lines per image size required
    imResize = im.resize((48, 48), Image.ANTIALIAS)
    imResize.save("icon-48x48.png", "PNG", quality=100)
    imResize = im.resize((72, 72), Image.ANTIALIAS)
    imResize.save("icon-72x72.png", "PNG", quality=100)
    imResize = im.resize((96, 96), Image.ANTIALIAS)
    imResize.save("icon-96x96.png", "PNG", quality=100)
    imResize = im.resize((144, 144), Image.ANTIALIAS)
    imResize.save("icon-144x144.png", "PNG", quality=100)
    imResize = im.resize((192, 192), Image.ANTIALIAS)
    imResize.save("icon-192x192.png", "PNG", quality=100)
    imResize = im.resize((256, 256), Image.ANTIALIAS)
    imResize.save("icon-256x256.png", "PNG", quality=100)
    imResize = im.resize((384, 384), Image.ANTIALIAS)
    imResize.save("icon-384x384.png", "PNG", quality=100)
    imResize = im.resize((512, 512), Image.ANTIALIAS)
    imResize.save("icon-512x512.png", "PNG", quality=100)


generate_icons(pic)
