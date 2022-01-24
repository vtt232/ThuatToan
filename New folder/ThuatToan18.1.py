# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 00:15:34 2022

@author: DELL
"""
def flip(arr, i):
	start = 0
	while start < i:
		temp = arr[start]
		arr[start] = arr[i]
		arr[i] = temp
		start += 1
		i -= 1


def sort(arr):
    kq=arr
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
            if kq[j] > kq[j+1] :
                kq[j], kq[j+1] = kq[j+1], kq[j]
    return kq
    


def countMinReverse(arr,n):
    start=[]
    start.extend(arr)
    dest=sort(arr)
    queu=[]
    queu.append([start,0])
    if(start==dest):
        return 0
    while len(queu)!=0:
        p=queu[0]
        t=p[0]
        queu.pop(0)
        for j in range(1,n):
            r=t
            flip(r,j)
            if r==dest:
                return p[1]+1
            queu.append([r,p[1]+1])
            
            
    
kq=countMinReverse([5,2,3,4,1], 5)
print(kq)