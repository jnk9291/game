import pygame as pg
from os import path

imgfolder = path.join(path.dirname(__file__), "assets","img")


def load_image(start,stop,imagename):
    imglist = []
    if start == stop:
        image = pg.image.load(path.join(imgfolder,imagename + ".png"))
        return image
    else:
        for i in range(start,stop+1):
            image = pg.image.load(path.join(imgfolder,imagename + str(i) + ".png"))
            imglist.append(image)
        return imglist