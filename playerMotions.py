import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
import pyautogui
from matplotlib.colors import rgb2hex
from directkeys import PressKey, ReleaseKey, W, A, S, D
from pathMath import findNearestWaypoint, bearingToWpt, distToWpt, parsePath
from gameData import getPlayerXY, getPlayerHeading


def wrapTo2pi(angle):
    posIn = angle>0
    angle = angle % 2*math.pi
    if angle == 0 and posIn:
        angle = 2*math.pi
    return angle

def turnToBearing(bearingCmd, heading):
    v = 1*math.pi
    err = (bearingCmd - heading)
    # if err > math.pi:
    #     err = ((2*math.pi) - err)*-1
    # if err < -math.pi:
    #     err = (2*math.pi) - (err*-1)
    t = abs((err)/v)
    if err < 0:
        PressKey(D)
        time.sleep(t)
        ReleaseKey(D)
    if err >= 0:
        PressKey(A)
        time.sleep(t)
        ReleaseKey(A)
    time.sleep(.1)

def walkToWpt(wpt):
    playerPos = getPlayerXY()
    playerHeading = getPlayerHeading()
    dist    = distToWpt(wpt, playerPos)
    bearing = bearingToWpt(wpt, playerPos)
    turnToBearing(bearing, playerHeading)
    PressKey(W)
    while dist > .05:
        playerPos = getPlayerXY()
        dist      = distToWpt(wpt, playerPos)
        #print(dist)
    print('walkToWpt: Made it! Moving on to next wpt...')
    ReleaseKey(W)

def followPath(path, loop):
    keepGoing = True
    wpts = parsePath(path)
    while(keepGoing): 
        playerPos = getPlayerXY()
        startingIdx = findNearestWaypoint(wpts, playerPos)-1
        for i in range(startingIdx, len(wpts)):
            walkToWpt(wpts[i])
        if loop:
            wpts.reverse()
        else:
            keepGoing = False
        

    


def main():
    print('Blah')
    
if __name__ == '__main__':  
    main()