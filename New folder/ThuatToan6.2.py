# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:16:29 2022

@author: DELL
"""


def sortQue(arr,k):
    for i in range(k):
        for j in range(0, k-i-1):
            if arr[j][0] > arr[j+1][0] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def mergeArrays(arrs, k):
    kq=[]
    priQue=[0]*k
    for i in range(k):
        priQue[i]=[arrs[i][0],i]
        arrs[i].pop(0)
        
    sortQue(priQue, k)
    
    while len(priQue)!=0:
        minElement=priQue[0]
        kq.append(minElement[0])
        priQue.pop(0)
        if len(arrs[minElement[1]])!=0:
            priQue.append([arrs[minElement[1]][0],minElement[1]])
            sortQue(priQue, k)
            arrs[minElement[1]].pop(0)
    print(kq)
    

        

    
    
arrs2=[[1,4,5],[1,3,4],[2,6]]
k=len(arrs2)
mergeArrays(arrs2,k)