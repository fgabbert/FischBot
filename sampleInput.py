import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
import pyautogui
from matplotlib.colors import rgb2hex
from directkeys import PressKey, ReleaseKey, W, A, S, D

# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)
# print('forward')
# PressKey(W)
# time.sleep(3)
# ReleaseKey(W)
# print('right')
# PressKey(D)
# time.sleep(3)
# ReleaseKey(D)

def int2Color(i):
    b = i % 256
    i = math.floor(i/256)
    g = i % 256
    i = math.floor(i/256)
    r = i % 256
    return np.array([r/255, g/255, b/255])

def decimal2Color(d):
    i = math.floor(d * 100000)
    return int2Color(i)

while(True):

    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    #screenshot.show()

    x_coord_pixel = np.asarray(screenshot.getpixel((4,1)))/255
    y_coord_pixel = np.asarray(screenshot.getpixel((9,1)))/255
    heading_pixel = np.asarray(screenshot.getpixel((14,1)))/255

    xcoord_hex  = rgb2hex(x_coord_pixel).split('#')[1]
    ycoord_hex  = rgb2hex(y_coord_pixel).split('#')[1]
    heading_hex = rgb2hex(heading_pixel).split('#')[1]

    xcoord  = round(int(xcoord_hex,16)/10000*10,2)
    ycoord  = round(int(ycoord_hex,16)/10000*10,2)
    heading = round(int(heading_hex,16)/100000*180/3.14159,2)
    print('X: ' + str(xcoord) + ' Y: ' + str(ycoord) + ' Heading: ' + str(heading))
    #print(ycoord)
    #print(heading)

    # for i in range(220):
    #     pixel = screenshot.getpixel((i,1))
    #     pixel_div = np.asarray(pixel)/255
    #     pixel_corr = rgb2hex(pixel_div)
    #     hexColor = pixel_corr.split('#')[1]
    #     decColor = int(hexColor,16)
    #     xcoord = decColor/100000*10
    #     print(int(hexColor,16)/10000*10)
    # print(decimal2Color(.4263))
    # test = rgb2hex(decimal2Color(.4263))
    # hexColor = test.split('#')[1]
    # print(hexColor)
    # print(int(hexColor,16)/10000*10)


    # # Tested the below code using hardcoded values from in-game and it freaking works..what the heck....
    # rgb_live = np.array([0, 0.65098039215686, 0.67058823529412])
    # test = rgb2hex(rgb_live)
    # hexColor = test.split('#')[1]
    # print(hexColor)
    # print(int(hexColor,16)/10000*10)

