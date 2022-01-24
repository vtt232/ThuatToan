# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:23:31 2022

@author: DELL
"""

def polygonArea(poly, n):
    XY=[0]
    X=[0]
    Y=[0]
    area=0
    for i in range(n):
        X.append(poly[i][0])
        Y.append(poly[i][1])
    for i in range(n):
        XY.append(X[i]*Y[i+1]-X[i+1]*Y[i])
    XY.append(X[n]*Y[1]-X[1]*Y[n])
    for i in range(len(XY)):
        area=area+XY[i]
    return abs(area / 2.0)
    
    

def dividePoly(n,i, j):
    poly1= list(range(i,j+1))
    poly2=list(range(j,n))
    poly2.extend(range(0,i+1))
    return poly1, poly2

def listPoints(points, poly):
    pointsSubPoly=[]
    for i in range(len(poly)):
        pointsSubPoly.append(points[poly[i]])
    return pointsSubPoly
    
    

def solve(points,n):
    minDelta=1000000
    kq=[-1,-1]
    for i in range(n):
        for j in range(i+2,n):
            if(i==0 and j==n-1):
                break
            poly1, poly2= dividePoly(n,i, j)
            pointsPoly1=listPoints(points, poly1)
            pointsPoly2=listPoints(points, poly2)
            areaPoly1=polygonArea(pointsPoly1, len(pointsPoly1))
            areaPoly2=polygonArea(pointsPoly2, len(pointsPoly2))
            deltaArea= abs(areaPoly1-areaPoly2)
            if(deltaArea<minDelta):
                minDelta=deltaArea
                kq=[points[i],points[j]]
    return kq
            
            
points=[(0,2),(0,0),(2,0),(3,3)]
print(solve(points, 4))

