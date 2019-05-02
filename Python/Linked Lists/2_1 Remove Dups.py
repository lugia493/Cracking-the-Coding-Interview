# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:23:39 2019

@author: Daniel
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeDups(head):
    n = head
    d = head
    while d.next != None:
        if n.val != d.val:
            n.next = d
            n = d
        d = d.next
    if n != d:
        n.next = d.next
    return head
    

def insert(head, node):
    if head.next is None:
        head.next = node
    else:
        insert(head.next, node)

def printNodes(head):
    while head != None:
        print(head.val)
        head = head.next
    
def main():
    head = Node(1)
    insert(head, Node(1))
    insert(head, Node(3))
    insert(head, Node(3))
    insert(head, Node(7))
    insert(head, Node(9))
    insert(head, Node(9))
    insert(head, Node(10))
    insert(head, Node(12))
    insert(head, Node(15))
    insert(head, Node(15))
    insert(head, Node(15))
    
    printNodes(head)
    print()
    h = removeDups(head)
    printNodes(h)
main()





    
    