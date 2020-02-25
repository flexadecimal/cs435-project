class bst:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def insertRec(root, val):
  if not root:
    root = bst(val)
    return;
  if val < root.val:
    insertRec(root.left, val)
  else:
    insertRec(root.right, val)

def inorder(root):
  out = []
  def helper(root):
  if root:
    helper(root.left)
    out.append(root.val)
    helper(root.right
  helper(root)
  return out
    
def bst_sort(unsorted):
  tree = bst(unsorted[0])
  for val in unsorted[1:]:
    insertRec(tree, val)
  return inorder(tree)