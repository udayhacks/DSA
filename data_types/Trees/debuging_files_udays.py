"""




# Python3 program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
        print(root.val)
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val, "values "),
 
        # now recur on right child
        printInorder(root.right)




def preOrder(root):
    print(root.val)
    
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    print("1",root)

    root.left = Node(2)
    print("2",root.left)

    root.right = Node(3)
    print("3",root.right)

    root.left.left = Node(4)
    print("4",root.left.left)

    root.left.right = Node(5)
    print("5",root.left.right)
 
    # Function call
    print ("\nInorder traversal of binary tree is")
    printInorder(root)"""





# Recursive Python program for level
# order traversal of Binary Tree
 
# A node structure
 
 
class Node:
 
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
 
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
 
""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
 
 
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        print(lheight,"left")
        rheight = height(node.right)
        print(rheight,"right")

 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
        






root = Node(1)
print("1",root)

root.left = Node(2)
print("2",root.left)

root.right = Node(3)
print("3",root.right)

root.left.left = Node(4)
print("4",root.left.left)

root.left.right = Node(5)
print("5",root.left.right)
 
 
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)
print(height(root))
