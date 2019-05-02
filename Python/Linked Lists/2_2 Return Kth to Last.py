# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:57:03 2019

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
    while head is not None:
        print(head.val)
        head = head.next
        
def kToLast(head, kth):
    if head is None:
        print("List is empty")
        return
    
    n = head
    counter = 1
    while n.next is not None:
        counter += 1
        n = n.next
    travel = counter - kth
    
    if travel < 0 :
        print("Cant do it")
        return
    n = head
    i = 0
    while n != None:
        if i == travel:
            return n.val
            break
        n = n.next
        i += 1
    return 

def main():
    head = Node(3)
    insert(head, Node(2))
    insert(head, Node(5))
    insert(head, Node(2))
    insert(head, Node(9))
    insert(head, Node(10))
    insert(head, Node(1))
    
    printNodes(head)
    
    print("Kth last element is", kToLast(head, 7))
main()
        