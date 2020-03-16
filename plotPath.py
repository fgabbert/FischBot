import numpy as np
import csv
import math
import matplotlib.pyplot as plt

def plotPath(filename):
    print('Plotting path: ' + filename)
    f = open(filename, newline='', encoding='utf-8')
    reader = csv.reader(f)
    xcoords = []
    ycoords = []
    for row in reader:
        xcoords.append(float(row[0]))
        ycoords.append(float(row[1]))
    plt.plot(xcoords,ycoords)
    plt.suptitle(filename)
    plt.show()

def main():
    plotPath('testPath.csv')
    
if __name__ == '__main__':  
    main()
    
    
    

