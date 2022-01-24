# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:55:11 2022

@author: DELL
"""
import math
def judgeSquareSum(n):
    i=0
    while(i*i<=n):
        b=math.sqrt(n-i*i)
        if(b%1==0):
            return [i,b]
        i=i+1
    return [0.1,0.1]



def fixDeltaNear(delta):
    if(delta[0]>delta[1]):
        tmp=delta[0]
        delta[0]=delta[1]
        delta[1]=tmp
    return delta

def fixDeltaOppo(delta):
    if(delta[0]<delta[1]):
        tmp=delta[0]
        delta[0]=delta[1]
        delta[1]=tmp
    return delta

def solve(s):
    points=[]
    deltaDisNear=judgeSquareSum(s)
    deltaDisOppo=judgeSquareSum(2*s)
    if(deltaDisNear==[0.1,0.1] or deltaDisOppo==[0.1,0.1]):
        points.append([0.1,0.1])
        return points
    else:
        deltaDisNear=fixDeltaNear(deltaDisNear)
        deltaDisOppo=fixDeltaOppo(deltaDisOppo)
        points.append([1,abs(deltaDisNear[1]-deltaDisOppo[1])])
        points.append([points[0][0]+deltaDisNear[0],points[0][1]+deltaDisNear[1]])
        points.append([points[0][0]+deltaDisOppo[0],points[0][1]+deltaDisOppo[1]])
        points.append([points[2][0]-deltaDisNear[0],points[2][1]-deltaDisNear[1]])
        return points
    
    

points=solve(5)
if(points[0]==[0.1,0.1]):
    print("IMPOSSIBLE")
else:
    print(points)

	

