'''
Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node
never differ by more than one.
'''
class Node:
    def __init__ (self,val):
        self.val = val
        self.right = None
        self.left = None

'''
This algorithm is 0(nlogn) because traversing a node in the tree takes
log n time but, because we are doing the getHeight() recurse for left and right
nodes of the root, we get 0(nlogn) complexity

Space is 0(H) where H is the max height of the tree due to recursive calls
'''
def getHeight1(root):
    if root is None:
        return -1
    return max(getHeight1(root.left),getHeight1(root.right)) + 1

def checkBalanced1(root):
    if root is None:
        return True
    heightDif = getHeight1(root.left) - getHeight1(root.right)
    if abs(heightDif) > 1:
        return False
    else:
        return checkBalanced1(root.left) and checkBalanced1(root.right)

'''
We can modify the above code by replacing the getHeight method.
If at any point we get an unbalanced tree, we could produce an error
and immediatly break once this happens. We also return the actual height of 
the tree rather than a boolean

-10 refers to the error produced
'''
def getHeight2(root):
    if root is None:
        return -1

    leftHeight = getHeight2(root.left)
    if leftHeight == -10:
        return -10

    rightHeight = getHeight2(root.right)
    if rightHeight == -10:
        return -10
    
    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return -10
    else:
        return max(leftHeight,rightHeight) + 1 
    
def checkBalanced2(root):
    return getHeight2(root) != -10

root = Node(2)
root.left = Node(7)
root.left.left = Node(2)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right = Node(5)
root.right.right = Node(5)
root.right.right.left = Node(4)

print(checkBalanced1(root))
print(checkBalanced2(root))