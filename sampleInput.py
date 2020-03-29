import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
import pyautogui
from matplotlib.colors import rgb2hex
from directkeys import PressKey, ReleaseKey, W, A, S, D, AB_1, AB_2, TAB
from pathMath import findNearestWaypoint, bearingToWpt, distToWpt, parsePath
from playerMotions import walkToWpt, followPath
from gameData import getPlayerXY, getCooldowns, getPlayerMana, getCombatStatus, getPlayerHeading, getPlayerHealth, getTargetName

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

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
 
loopit = True
while(loopit):
    followPath('westfallEdge.csv',True)
    #wpts = parsePath('testPath1.csv')
    #walkToWpt(wpts[0])
    #tgt = getPlayerMana()
    #print(tgt)
    #loopit = False


