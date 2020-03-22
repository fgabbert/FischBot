import numpy as np
import csv
import math
import matplotlib.pyplot as plt

def distToWpt(wpt,playerPos):
    tmp = math.sqrt(((playerPos[0]-wpt[0])**2 + (playerPos[1]-wpt[1])**2))
    return tmp

def parsePath(path):
    f = open(path, newline='', encoding='utf-8')
    reader = csv.reader(f)
    wpts = []
    for row in reader:
        wpts.append([float(row[0]),float(row[1])])
    return wpts


def findNearestWaypoint(wpts, playerPos):
    dist = 9999.99
    idx = 0
    for wpt in wpts:
        tmp = math.sqrt(((playerPos[0]-wpt[0])**2 + (playerPos[1]-wpt[1])**2))
        if tmp<dist:
            dist = tmp
            idx = idx+1
    return idx
             
def bearingToWpt(wpt, playerPos):
    bearing = math.atan2((wpt[1]-playerPos[1]), (playerPos[0]-wpt[0])) + math.pi - math.pi*.5
    if bearing < 0:
        bearing = bearing + 2*math.pi
    if bearing > 2*math.pi:
        bearing = bearing - 2*math.pi
    return bearing

def main():
    closestWpt = findNearestWaypoint('gs2ns.csv',[45.8, 59.4])
    print(closestWpt)
    
if __name__ == '__main__':  
    main()
    
    
     

