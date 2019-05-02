# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:21:44 2019

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

def detector(head):
    slow = head
    fast = head.next
    while fast.next is not None and fast.next.next is not None:
        if slow is fast:
            return slow.val
        slow = slow.next
        fast = fast.next.next
    return -1

def main():
    loopNode = Node("C")
    
    head = Node("A")
    insert(head, Node("B"))
    insert(head, loopNode)
    insert(head, Node("D"))
    insert(head, Node("E"))
    insert(head, loopNode)
    
    print(detector(head))
main()