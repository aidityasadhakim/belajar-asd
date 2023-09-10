class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        # Traverse the left
        inorder(root.left)
        print(root.data, end=" ")
        # Traverse the right
        inorder(root.right)

def postorder(root):
    if root:
        # Traverse the left
        postorder(root.left)
        # Traverse the right
        postorder(root.right)
        # Traverse the root
        print(root.data, end=" ")

def preorder(root):
    if root:
        # Traverse the root
        print(root.data, end=" ")
        # Traverse the left
        preorder(root.left)
        # Traverse the right
        preorder(root.right)

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(11)
root.left.left = Node(7)
root.left.right = Node(8)

print("Post Order:")
postorder(root)
print("\nIn order: ")
inorder(root)
print("\nPre order: ")
preorder(root)

'''
    5
   / \
  10  15
  /\   /\
 7  8 12 11

7 -> 8 -> 10 -> 15 -> 5
7 -> 10 -> 8 -> 5 -> 15 
5 -> 10 -> 7 -> 8 -> 15 -> 12 -> 11
'''