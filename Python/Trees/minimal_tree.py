'''
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
'''

class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

def minimalTree(arr):
    return helper(arr,0,len(arr)-1)
    
def helper(arr,start,end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = Node(arr[mid])
    n.left = helper(arr,start,mid-1)
    n.right = helper(arr,mid+1,end)
    return n

arr = [1,2,3,4,5,6,7,8,9,10]
root = minimalTree(arr)

# To verify
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

inorder(root)