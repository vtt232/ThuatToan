# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:36:29 2022

@author: DELL
"""
from math import sqrt
size = 1001
prime = [0 for i in range(size)]


def sieve(n):
    kq=0
    prime[0] = 1
    prime[1] = 1
    for i in range(2, int(sqrt(2*n)) + 1, 1):
        if (prime[i] == 0):
            for j in range(i*2, 2*n, i):
                prime[j] = 1
    for i in range(2, n+1, 1):
        for p in range(2, i+1, 1):
            q=2*i-p
            if (prime[p] == 0 and prime[q] == 0):
                kq=kq+1
    return kq

def solve(n):
    kq=sieve(n)
    return kq

print(solve(9))