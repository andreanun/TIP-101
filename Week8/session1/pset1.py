#Problem 1: Build a Binary Tree I
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
#or 
#root = TreeNode(5, TreeNode(3), TreeNode(1))

#Problem 2: 3-Node Sum I
def check_tree(root):
  left = root.left.val
  right = root.right.val

  if root.val == left + right:
    return True
  else:
    return False

print(check_tree(root))

#Problem 3: 3-Node Sum II
class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree(root):
  left = 0
  right = 0
  if not root:
    return False
  if root.left:
    left = root.left.val
  if root.right:
    right = root.right.val
  if root.val == left + right:
    return True
  else:
    return False

root = None
print(check_tree(root))

# Problem 4
recursive call left_most, go until root.left = None
def left_most(root):
  if not root:
    return None
  if not root.left:
    return root.val
  return left_most(root.left)

root = TreeNode(1, None, TreeNode(5, TreeNode(3)))
print(left_most(None))

# Problem 5
class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most(root):
  if not root:
    return None
  if not root.left:
    return root.val
  while root.left is not None:
    root = root.left
  return root.val

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(None))

#Problem 6: In-order Traversal
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def inorder_traversal(root):
  lst = []
  if root:
    lst = inorder_traversal(root.left)
    lst.append(root.val)
    lst = lst + inorder_traversal(root.right)
  return lst

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(root))

#Problem 7: Binary Tree Size
def size(root):
  if not root:
    return 0
  return 1 + size(root.left) + size(root.right)

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(size(root))

#Problem 8
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def find(root, value):
  if not root:
    return False
  if root.val == value:
    return True
  return find(root.left, value) | find(root.right, value)

root = TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(3)))
print(find(root, 2))

#Problem 9: Binary Search Tree Find
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def find_bst(root, value):
  if not root:
    return False
  if root.val == value:
    return True
  if value < root.val:
    return find_bst(root.left, value)
  elif value > root.val:
    return find_bst(root.right, value)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(find_bst(root, 10))

#Problem 10: BST Descending Leaves
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

  def collect_leaves_descending(root, leaves):
    """
    Helper function to collect leaf nodes' values from the BST rooted at `root` in descending order.
    The values are collected directly into the list `leaves`.
    """
    if root is None:
        return

    # First, visit the right child (to ensure descending order)
    collect_leaves_descending(root.right, leaves)

    # Check if it's a leaf node
    if root.left is None and root.right is None:
        leaves.append(root.val)

    # Then, visit the left child
    collect_leaves_descending(root.left, leaves)

  def descending_leaves(root):
    """
    Return a list of leaf values in descending order from the BST rooted at `root`.
    """
    leaves = []
    collect_leaves_descending(root, leaves)
    return leaves