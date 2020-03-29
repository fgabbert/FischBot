import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
import pyautogui
from matplotlib.colors import rgb2hex
from directkeys import PressKey, ReleaseKey, ESC, G, W, A, S, D, AB_1, AB_2, AB_3, AB_4, TAB, Q
from pathMath import findNearestWaypoint, bearingToWpt, distToWpt, parsePath
from gameData import getPlayerXY, getCombatStatus, getPlayerHeading, getPlayerHealth, getPlayerMana, getTargetName


def wrapTo2pi(angle):
    posIn = angle>0
    angle = angle % 2*math.pi
    if angle == 0 and posIn:
        angle = 2*math.pi
    return angle

def turnToBearing(bearingCmd, heading):
    v = 1*math.pi
    err = (bearingCmd - heading)
    if err > math.pi:
        err = ((2*math.pi) - err)*-1
    if err < -math.pi:
        err = (2*math.pi) - (err*-1)
    t = abs((err)/v)
    if err < 0:
        PressKey(D)
        time.sleep(t)
        ReleaseKey(D)
    if err >= 0:
        PressKey(A)
        time.sleep(t)
        ReleaseKey(A)
    #time.sleep(.1)

def walkToWpt(wpt):
    playerPos = getPlayerXY()
    playerHeading = getPlayerHeading()
    dist    = distToWpt(wpt, playerPos)
    bearing = bearingToWpt(wpt, playerPos)
    turnToBearing(bearing, playerHeading)
    PressKey(W)
    tgtTimer = 0
    while dist > .1:
        tgt = checkTarget()
        if tgt:
            ReleaseKey(W)
            time.sleep(.1)
            fightTarget()
            walkToWpt(wpt)
        playerPos = getPlayerXY()
        playerHeading = getPlayerHeading()
        bearing = bearingToWpt(wpt, playerPos)
        if abs(bearing - playerHeading) > 10*math.pi/180:
            turnToBearing(bearing, playerHeading)
            dist = distToWpt(wpt, playerPos)
        PressKey(W)
    print('walkToWpt: Made it! Moving on to next wpt...')
    ReleaseKey(W)

def checkTarget():
    PressKey(TAB)
    ReleaseKey(TAB)
    tgt = getTargetName()
    return tgt != 0

def healSelf():
    health = getPlayerHealth()
    time.sleep(.5)
    if health < 60:
        print('Healing! Health is: ' + str(health))
        PressKey(AB_2)
        ReleaseKey(AB_2)
        time.sleep(5) # Heals take around 3 sec to cast with a mob on you
        health = getPlayerHealth()

def lootMob():
    print('Looting Mob!')
    PressKey(G)
    ReleaseKey(G)
    PressKey(Q)
    ReleaseKey(Q)
    time.sleep(.2)
    PressKey(ESC)
    ReleaseKey(ESC)

def fightTarget():
    # Stop Running and engage "interact with target"
    print('fightTarget: Stop running')

    # Cast Seal of Righteousness
    print('fightTarget: Seal')
    PressKey(AB_3)
    ReleaseKey(AB_3)
    
    # Wait until we enter combat....give up if it took longer than 30 seconds
    cbt = 0
    while cbt == 0:
        print('fightTarget: Waiting for combat')
        PressKey(Q)
        ReleaseKey(Q)
        time.sleep(2)
        cbt = getCombatStatus()
    print('In combat!')

    while cbt == 1:
        print('fightTarget: Waiting to drop combat')
        PressKey(Q)
        ReleaseKey(Q)
        PressKey(AB_1)
        ReleaseKey(AB_1)
        healSelf()
        cbt = getCombatStatus()
        time.sleep(1)
    # While in combat, use judgement on CD and check if we need to heal
    
    # After combat, loot the mob and check if we need to drink
    lootMob()
    print('fightTarget: Done fighting!')
    mana = getPlayerMana()
    if mana < 50:
        print('Need to drink...')
        PressKey(AB_4)
        ReleaseKey(AB_4)
        while mana < 95:
            time.sleep(1)
            mana = getPlayerMana()


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