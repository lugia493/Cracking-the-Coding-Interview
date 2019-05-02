'''
Validate BST: Implement a function to check if a binary tree is a binary search tree.
'''

'''
Inorder traversal could print the nodes in order
'''

class Node:
    def __init__ (self,val):
        self.val = val
        self.right = None
        self.left = None

'''
First Solution

Inorder traversal of a BST will present all of the nodes in sorted order
We could populate an arr with these node values and check if the array is sorted
linearly in 0(n) time. 

The following is the iterative method. 
This method doesnt pass the condition root.val <= right.val
if this is a requirment for BST
'''

def helper(arr, root):
    # Populate the array as we perform inorder traversal
    if root:
        helper(arr, root.left)
        arr.append(root.val)
        helper(arr, root.right)

def isBST(root):
    # Define the sorted array
    arr = []
    # Populate the array using inorder traversal
    helper(arr, root)
    # Check that the values are sorted in 0(n) time
    for i in range(1,len(arr)):
        # return False if not sorted
        if arr[i-1] <= arr[i]:
            return False
    # return true if the array is sorted
    return True

root = Node(2)
root.left = Node(7)
root.left.left = Node(2)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right = Node(5)
root.right.right = Node(5)
root.right.right.left = Node(4)

print(isBST(root))

''' 
Note: the array is actually not necessary. We just care about comparing
the previous element in this approach. We could simplify the solution
furthur.
'''

def checkBST(root):
    if root is None:
        return True
    # Recurse/check left child
    if not checkBST(root.left):
        return False
    # Check if prev is not -1 and if current node is less then prev
    if checkBST.prev != -1 and root.val <= checkBST.prev:
        return False
    # After the check, assign the current node to the prev variable
    checkBST.prev = root.val
    # Recurse/check right child
    if not checkBST(root.right):
        return False
    # If we get through the recursion, we are good
    return True

checkBST.prev = -1
print(checkBST(root))


'''

Solution 2:

Sense all nodes on the left must be less than root.val and same with all right node values
We can keep track of a min and a max, which is populated by the root.val
Max will be updated when we traverse left, and min when we travese right.

Always make sure that base cases and null cases are well handled

'''

def findifBST(root):
    return helper(root, -1, -1)

def helper(root,min,max):
    if root is None:
        return True
    if min != -1 and root.val <= min or max != -1 and root.val > max:
        return False
    if not helper(root.left,min,root.val) or not helper(root.right,root.val,max):
        return False
    return True





