# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:44:12 2019

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

def printNode(head):
    if head is None:
        return
    print(head.val)
    printNode(head.next)

def main():
    
    head = Node(3)
    insert(head, Node(5))
    insert(head, Node(8))
    insert(head, Node(5))
    insert(head, Node(10))
    insert(head, Node(2))
    insert(head, Node(1))
    
    printNode(head)
main()