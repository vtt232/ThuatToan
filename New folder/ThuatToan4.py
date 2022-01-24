# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:36:46 2022

@author: DELL
"""

def getSum( BITree, index):
    sum = 0 
     
    while (index > 0):
        sum += BITree[index]
        index -= index & (-index) 
    return sum
 

def updateBIT(BITree, n, index, val):
    while (index <= n):
        BITree[index] += val
        index += index & (-index)
 
def getInvCount(arr, n):
 
    invcount = 0 
    maxElement = max(arr)
 
    BIT = [0] * (maxElement + 1)
    for i in range(1, maxElement + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        invcount += getSum(BIT, arr[i] - 1)
        updateBIT(BIT, maxElement, arr[i], 1)
    return invcount

print(getInvCount([1,2,4,3,5,1],6))