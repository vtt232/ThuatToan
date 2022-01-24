# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:05:21 2022

@author: DELL
"""

import math


def findPos(index, numbers,n):
    smallerNum=0
    for j in range(index+1, n):
        if (numbers[j] < numbers[index]):
            smallerNum += 1
    return smallerNum

def permutationIndex(numbers):
  numbers.insert(0, 0)
  n=len(numbers)
  kq=0
  for i in range (1,n):
      pos=findPos(i, numbers, n)
      kq=kq+pos*math.factorial(n-i-1)
  return kq+1

def indexPermutation(n,index):
    numbers=[0]*(n+1)
    check=list(range(0, n+1))
    for i in range(1,n):
        per=math.factorial(n-i)
        pos=math.ceil(index/per)
        numbers[i]=check[pos]
        index=index-per*(numbers[i]-1)
        check.remove(numbers[i])
    numbers[n]=check[-1]
    numbers.pop(0)
    return numbers
        




print(permutationIndex([1,3,2]))
print(indexPermutation(3, 6))