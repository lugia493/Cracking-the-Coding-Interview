# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:25:41 2019

@author: Daniel
"""

class Node:
    def __init__ (self, val):
        self.val = val
        self.next = None
        
def insert(head, node):
    if head.next is None:
        head.next = node
    else:
        insert(head.next,node)
        
def printNode(head):
    if head is None:
        return
    else:
        print(head.val)
        printNode(head.next)

def delete_middle_node(head, node):
    if head.val is node.val:
        return head
    curr = head
    prev = None
    
    while curr.next is not None:
        if curr.val is node.val:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next
    return head
    
    
def main():
    
    head = Node("a")
    insert(head, Node("b"))
    insert(head, Node("c"))
    insert(head, Node("d"))
    insert(head, Node("e"))
    insert(head, Node("f"))
    
    printNode(head)
    print()
    delete_middle_node(head, Node("d"))
    printNode(head)

    
main()