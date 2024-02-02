# Resizes an image and keeps aspect ratio. Set mywidth to the desired with in pixels.

import PIL
import os
from PIL import Image

my_width = 2500
src_dir = '/Users/uche4/OneDrive/Desktop/images'
des_dir = '/Users/uche4/OneDrive/Desktop/images1'


def resize_image(old_pix, new_pix, my_width):
    img = Image.open(old_pix)
    wpercent = (my_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((my_width, hsize), PIL.Image.ANTIALIAS)
    img.save(new_pix)


def all_dir(src_dir, des_dir, width):
    files = os.listdir(src_dir)

    i = 0
    for file in files:
        i += 1
        old_pix = src_dir + '/' + file
        new_pix = des_dir + '/' + file
        resize_image(old_pix, new_pix, width)
        print(i, 'Done')


all_dir(src_dir, des_dir, my_width)