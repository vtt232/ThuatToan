# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:58:31 2022

@author: DELL
"""
from itertools import combinations


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def pathToNode(root, path, k):

    if root is None:
        return False


    path.append(root.data)
 

    if root.data == k :
        return True
 
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right!= None and pathToNode(root.right, path, k))):
        return True

    path.pop()
    return False

def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)

        path2 = []
        pathToNode(root, path2, data2)

        i=0
        while i<len(path1) and i<len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1

        return (len(path1)+len(path2)-2*i)
    else:
        return 0
    
def addNode(root, edge):
    if root:
        if root.data==edge[0]:
            if root.left == None:
                root.left=Node(edge[1])
                return True
            elif root.right ==None:
                root.right=Node(edge[1])
                return True
            else:
                return False
        if addNode(root.left, edge) or addNode(root.right, edge):
            return True
        return False
            
    
    
def createTree(arrs, n):
    root=Node(arrs[0][0])
    for i in range(len(arrs)):
        addNode(root, arrs[i])
    return root
    

root=createTree([[1,2],[1,3],[3,4],[3,5]], 5)

sum=0 
comb = combinations([1,2,3,4,5], 2)
for item in list(comb):
    sum+=distance(root, item[0], item[1])
print(sum)
