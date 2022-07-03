# HariFun 208 - Polymorphy
# by Hari Wiguna, 2022

import st7789
import tft_config
import math
import time

tft = tft_config.config(0)

x0, y0 = 135/2, 240/2
r = y0/2
numPoints = 36
numFrames = 10

def poly(numVertex,rotation):
    list = []
    rot = - 2*math.pi *(rotation)/360
    reps = numPoints/numVertex
    for i in range(numVertex):
        a = rot+ 2*math.pi * i/numVertex
        x = int(x0 + math.sin(a)*r)
        y = int(y0 + math.cos(a)*r)
        
        for spread in range(int(reps)):
            list.append((x,y))
    
    list.append(list[0])
    return list

def circle():
    return poly(36,0)

def triangle():
    return poly(3,30)

def square():   
    return poly(4,45)

def hexagon():   
    return poly(6,-30)

def star(numVertex,rotation):
    list = []
    rot = - 2*math.pi *(rotation)/360
    r2 = r/3
    for i in range(numVertex):
        a2 = rot + 2*math.pi * i/numVertex
        a1 = a2 - 2*math.pi * 1/numVertex/3
        a3 = a2 + 2*math.pi * 1/numVertex/3
        x1 = int(x0 + math.sin(a1)*r2)
        y1 = int(y0 + math.cos(a1)*r2)

        x2 = int(x0 + math.sin(a2)*r)
        y2 = int(y0 + math.cos(a2)*r)

        x3 = int(x0 + math.sin(a3)*r2)
        y3 = int(y0 + math.cos(a3)*r2)

        list.append((x1,y1))
        list.append((x2,y2))
        list.append((x3,y3))
    
    list.append(list[0])
    return list

def computeFrame( startShape, endShape, frameNum):
    list = []
    for i in range(min(len(startShape),len(endShape))):
        endPoint = endShape[i]
        startPoint = startShape[i]
        x = int(startPoint[0] + (endPoint[0]-startPoint[0])*frameNum/numFrames)
        y = int(startPoint[1] + (endPoint[1]-startPoint[1])*frameNum/numFrames)
        list.append((x,y))
    
    return list

def morph(startShape,endShape):
    for i in range(numFrames):       
        frame = computeFrame(startShape,endShape,i)
        tft.fill(st7789.BLACK)
        tft.polygon(frame, 0,0, st7789.YELLOW, 0, 0, 0)
        time.sleep(0.1)

def main():
    tft.init()

    tri = triangle()
    cir = circle()
    sqr=square()
    hex=hexagon()
    str=star(12,0)
    
    while True:
        morph(str,tri)
        morph(tri,str)
        
        morph(str,sqr)
        morph(sqr,str)
        
        morph(str,hex)
        morph(hex,str)
        
        morph(str,cir)
        morph(cir,str)
       
main()
