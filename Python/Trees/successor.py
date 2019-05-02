'''
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node 
in a binary search tree. You may assume that each node has a link to its parent.
'''


'''
Binary Search Tree created below
'''
class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)


def successor(node):
    '''
    Base case: if node is None, we could easily return Nonde
    '''
    if node is None:
        return None
    
    '''
    In the LNR process, if node.right is not None, then we are at the N step. We need to do to R step
    and futhermore do LNR traversal there, which calls for us to find L first. Therefore, we need to print the left-most 
    node of Node is Node.right is not None
    '''
    if node.right is not None:
        return leftMostNode(node.right)
    else:
        ''' 
        There is two cases about printing the next Node if node.right is None

        In the first case, we can have two smaller cases that will essentially use the same code.

            Node is left of parent or Node is right of parent

            In case 1, We simply bubble up to parent, and pring parent's valid, as L subtree is done, and now N is printed in inorder traversal
            In case 2, that means parent is done traversing, which means that parent's parent is at L step in inorder traversal, thus we need to 
            print out the parent's parent node in the LNR process. This could happend to parent's parent's parent node as well. But this is essentially 
            the same as step 1, where we print the N process in LNR traversal.

            We could use a while loop to check for these cases:
        
            In both cases, we bubble up until we find a parent node (untraversed) who's
            child node (the same Node mentioned in the above paragraph) is its left child. 
            We print N in the LNR process because L is completed.
            Therefore, if we say q = Node and x = Node.parent, then we 
            terminate the while loop when node q is the left child of parent x. 

        In the second case, we mention the edge case which is when the Node is the last node in inorder traversal
            
            If the q is the last node in inorder traversal (i.e. futherest right node), then we dont have another node to print. 
            We must break the while loop if x becomes None.

            Therefore, we traverse the parents nodes if x is not None and x.left is not q. Then we print x, which could either be None, or the N step in LNR

        In either case, we return the parent node, which could have a value or be None, depending on the condition that terminates the while loop.

        '''
        q = node
        x = q.parent
        while x is not None and x.left != q: 
            q = x
            x = x.parent
        return x

'''
Get the left most child, terminate when node.left is None
'''
def leftMostNode(node):
    while n.left is not None:
        n = n.left
    return n

