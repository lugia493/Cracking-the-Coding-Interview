'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all 
the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

class TreeNode:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None

def minimalTree(arr):
    return helper(arr,0,len(arr)-1)

def helper(arr,start,end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = TreeNode(arr[mid])
    n.left = helper(arr,start,mid-1)
    n.right = helper(arr,mid+1,end)
    return n

arr = [1,2,3,4,5,6,7,8,9,10]
root = minimalTree(arr)

'''
Answer below

'''
from collections import deque
import numpy as np 

def listOfDepths(root):
    q = deque()
    q.append(root)
    res = []
    while q:
        count = len(q)
        head = Node(0)
        realHead = head
        while count > 0:
            n = q.popleft()
            head.next = Node(n.val)
            head = head.next
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
            count -= 1
        res.append(realHead.next)
    return res

res = listOfDepths(root)

for ll in res:
    while ll is not None:
        print(ll.val)
        ll = ll.next
    print
