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

def getCombatStatus():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    combat_pixel = np.asarray(screenshot.getpixel((54,1)))/255
    combat_hex = rgb2hex(combat_pixel).split('#')[1]
    combat = round(int(combat_hex,16),2)
    return combat


def getTargetName():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    tgt_pixel = np.asarray(screenshot.getpixel((66,1)))/255
    tgt_hex = rgb2hex(tgt_pixel).split('#')[1]
    tgt = round(int(tgt_hex,16),2)
    return tgt

def getCooldowns():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    cd_pixel = np.asarray(screenshot.getpixel((140,1)))/255
    cd_hex = rgb2hex(cd_pixel).split('#')[1]
    cd = round(int(cd_hex,16),2)
    return cd

def getPlayerHealth():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    maxHealth_pixel = np.asarray(screenshot.getpixel((40,1)))/255
    maxHealth_hex = rgb2hex(maxHealth_pixel).split('#')[1]
    maxHealth = round(int(maxHealth_hex,16),2)

    currHealth_pixel = np.asarray(screenshot.getpixel((44,1)))/255
    currHealth_hex = rgb2hex(currHealth_pixel).split('#')[1]
    currHealth = round(int(currHealth_hex,16),2)

    healthPercent = int((currHealth/maxHealth)*100)
    return healthPercent

def getPlayerMana():
    screenshot = ImageGrab.grab(bbox=(0,0,220,4))
    maxMana_pixel = np.asarray(screenshot.getpixel((48,1)))/255
    maxMana_hex   = rgb2hex(maxMana_pixel).split('#')[1]
    maxMana       = round(int(maxMana_hex,16),2)

    currMana_pixel = np.asarray(screenshot.getpixel((52,1)))/255
    currMana_hex   = rgb2hex(currMana_pixel).split('#')[1]
    currMana       = round(int(currMana_hex,16),2)

    manaPercent = int((currMana/maxMana)*100)
    return manaPercent
