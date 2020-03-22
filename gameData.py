import numpy as np
from PIL import ImageGrab
import time
import math
from matplotlib.colors import rgb2hex

def getPlayerXY():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))

    x_coord_pixel = np.asarray(screenshot.getpixel((4,1)))/255
    y_coord_pixel = np.asarray(screenshot.getpixel((9,1)))/255
    heading_pixel = np.asarray(screenshot.getpixel((14,1)))/255

    xcoord_hex  = rgb2hex(x_coord_pixel).split('#')[1]
    ycoord_hex  = rgb2hex(y_coord_pixel).split('#')[1]
    heading_hex = rgb2hex(heading_pixel).split('#')[1]

    xcoord  = round(int(xcoord_hex,16)/10000*10,2)
    ycoord  = round(int(ycoord_hex,16)/10000*10,2)
    playerPos = [xcoord, ycoord]
    return playerPos

def getPlayerHeading():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    heading_pixel = np.asarray(screenshot.getpixel((14,1)))/255
    heading_hex = rgb2hex(heading_pixel).split('#')[1]
    heading = round(int(heading_hex,16)/100000,2)
    return heading
