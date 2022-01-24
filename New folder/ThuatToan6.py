# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:21:24 2022

@author: DELL
"""

def mergeTwoArrays(l, r):

    ret = []
 
    l_in, r_in = 0, 0
 
    while l_in + r_in < len(l) + len(r):
        if (l_in != len(l) and (r_in == len(r) or l[l_in] < r[r_in])):
            ret.append(l[l_in])
            l_in += 1
        else:
            ret.append(r[r_in])
            r_in += 1
 
    return ret
 
def mergeArrays(arrs,k):

    arr_s = []

    while len(arrs) != 1:
        arr_s[:] = []
        for i in range(0, len(arrs), 2):
            if i == len(arrs) - 1:
                arr_s.append(arrs[i])
 
            else:
                arr_s.append(mergeTwoArrays(arrs[i],arrs[i + 1]))
        arrs = arr_s[:]

    return arrs[0]
 
    


arrs1 = [[ 5, 7, 15, 18 ],[ 1, 8, 9, 17 ],[ 1, 4, 7, 7 ]];
arrs2=[[1,4,5],[1,3,4],[2,6]]
k=len(arrs2)
kq= mergeArrays(arrs2,k)
print(kq)