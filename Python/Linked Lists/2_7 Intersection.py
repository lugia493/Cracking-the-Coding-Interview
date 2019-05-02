# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:53:13 2019

@author: Daniel
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def insert(head, node):
    if head.next is None:
        head.next = node
    else:
        insert(head.next, node)

def printNodes(head):
    if head is None:
        return
    print(head.val)
    printNodes(head.next)

def intersection(l1, l2):
    if l1.next is None or l2.next is None:
        return -1
    
    
    len1 = 0
    len2 = 0
    a = l1
    b = l2
    while a.next is not None:
        len1 = len1 + 1
        a = a.next
    while b.next is not None:
        len2 = len2 + 1
        b = b.next
        
    a = l1
    b = l2
    
    if len2 > len1:
        for i in range(0, len2 - len1):
            b = b.next
    else:
         for i in range(0, len1 - len2):
            a = a.next
            
    while a.next is not None and b.next is not None:
        if a is b:
            return a.val
        a = a.next
        b = b.next
    return -1
    
def main():
    l1 = Node(1)
    insert(l1, Node(2))
    insert(l1, Node(3))
    insert(l1, Node(4))
    insert(l1, Node(5))

    l2 = Node(1)
    insert(l2, Node(2))
    insert(l2, l1.next.next.next)
    
    printNodes(l2)
        
    print(intersection(l1, l2))
main()