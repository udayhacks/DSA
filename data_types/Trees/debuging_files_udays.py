




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
    printInorder(root)