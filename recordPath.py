import numpy as np
from PIL import ImageGrab
import cv2
import csv
import os
import time
import math
import pyautogui
from plotPath import plotPath
from matplotlib.colors import rgb2hex

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

x_coords = []
y_coords = []
filename = input('Enter path name: ')
filename = filename +'.csv'
# Check if filename already exists and delete if so
if os.path.exists(filename):
  os.remove(filename)
# Open up the new file to start writing the path to
f = open(filename, 'w', newline='')
writer = csv.writer(f)

for i in list(range(3))[::-1]:
    print('Begin recording path in: ' + str(i+1))
    time.sleep(1)
keepGoing = True
xcoord_z = -999.99
ycoord_z = -999.99
while(keepGoing):
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))

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
    if (xcoord==xcoord_z and ycoord==ycoord_z):
        keepGoing = False
    x_coords.append(xcoord)
    y_coords.append(ycoord)
    xycoord = [xcoord, ycoord]
    writer.writerow(xycoord)
    xcoord_z = xcoord
    ycoord_z = ycoord
    time.sleep(2)
f.close()
print('Path recorded!')
plotPath(filename)

    
    
    

