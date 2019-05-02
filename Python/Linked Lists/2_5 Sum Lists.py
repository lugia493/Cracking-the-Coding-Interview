# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:23:39 2019

@author: Daniel
"""

class Node:
    def __init__ (self, val):
        self.val = val
        self.next= None
        
def printNodes(head):
    if head is None:
        return
    print(head.val)
    printNodes(head.next)
    
def insert(head, node):
    if head.next is None:
        head.next = node
    else:
        insert(head.next, node)
        
def add(exp1, exp2):
    if exp1 is None:
        return exp2
    elif exp2 is None:
        return exp1
    
    head = Node(0)
    new_head = head
    carry = 0
    while exp1 and exp2:
        temp = exp1.val + exp2.val + carry
        carry = temp // 10
        ones = temp % 10
        tempNode = Node(ones)
        head.next = tempNode
        head = head.next
        exp1 = exp1.next
        exp2 = exp2.next
    while exp1:
        temp = carry + exp1.val
        carry = temp // 10
        ones = temp % 10
        tempNode = Node(ones)
        head.next = tempNode
        head = head.next
        exp1 = exp1.next
    while exp2:
        temp = carry + exp2.val
        carry = temp // 10
        ones = temp % 10
        tempNode = Node(ones)
        head.next = tempNode
        head = head.next
        exp2 = exp2.next
    if carry > 0:
        head.next = Node(carry)
    return new_head.next

def main():
    exp1 = Node(7)
    insert(exp1, Node(1))
    insert(exp1, Node(9))
    insert(exp1, Node(9))
    printNodes(exp1)
    
    print()
    exp2 = Node(5)
    insert(exp2, Node(9))
    insert(exp2, Node(2))
    printNodes(exp2)
    print()
    head = add(exp1, exp2)
    printNodes(head)
main()
