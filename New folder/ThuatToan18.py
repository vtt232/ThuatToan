# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:08:59 2022

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


def findMax(arr, n):
	mi = 0
	for i in range(0,n):
		if arr[i] > arr[mi]:
			mi = i
	return mi


def pancakeSort(arr, n):
    flipTimes=0
    curr_size = n
    while curr_size > 1:
        mi = findMax(arr, curr_size)
        if mi != curr_size-1:
            flip(arr, mi)
            flip(arr, curr_size-1)
            flipTimes=flipTimes+2
        curr_size -= 1
    return flipTimes


arr = [5,2,3,4,1]
n = len(arr)
times=pancakeSort(arr, n);
print(times)

