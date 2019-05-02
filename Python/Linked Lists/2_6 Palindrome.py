# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:56:06 2019

@author: Daniel
"""
from collections import deque

class Node:
    def __init__ (self, val):
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
    
def reverse(head):
    start = None
    while head is not None:
        temp = Node(head.val)
        temp.next = start
        start = temp
        head = head.next
    return start

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    
    reverse_head = reverse(head)

    while reverse_head.next is not None:
        if reverse_head.val != head.val:
            return False
        reverse_head = reverse_head.next
        head = head.next
    return True
    
def isPalindrome2(head):
    fast = head
    slow = head
    
    stack = deque()
    while fast is not None and fast.next is not None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
        
    if fast is not None: #off elements, skip the middle
        slow = slow.next
    print(stack)
    while slow is not None:
        top = stack.pop()
        if top != slow.val:
            return False
        slow = slow.next
    return True

def main():
    head = Node("r")
    insert(head, Node("a"))
    insert(head, Node("c"))
    insert(head, Node("e"))
    insert(head, Node("c"))
    insert(head, Node("a"))
    insert(head, Node("r"))

    print(isPalindrome(head))
    print(isPalindrome2(head))
    
    
main()