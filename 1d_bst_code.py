class bst:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def insertIter(root, val):
  new_node = bst(val)
  cursor = root
  prev = None
  while cursor is not None:
    prev = cursor
    if val < cursor.val:
      cursor = cursor.left
    else:
      cursor = cursor.right
  # empty tree
  if prev is None:
    prev = new_node
  # insert into left
  elif val < prev.val:
    prev.left = new_node
  # insert into right
  else:
    prev.right = new_node 

def deleteIter(root, val):
  cursor = root
  prev = None
  to_delete = None
  # find node to delete, and parent
  while cursor is not None:
    prev = cursor
    if cursor.val == val:
      to_delete = cursor
    if val < cursor.val:
      cursor = cursor.left
    else:
      cursor = cursor.right
  # leaf case
  if to_delete.left is None and to_delete.right is None:
    # leaf is root
    if to_delete is root:
      root = None
    # leaf is left
    if prev.left is to_delete:
      prev.left = None
    else:
    # leaf is right
      prev.right = None
  # 1 child cases
  # node to delete has right child
  elif to_delete.left is None:
    # delete root
    if to_delete is root:
      root = to_delete.right
    # to_delete is left child
    elif prev.left is to_delete:
      prev.left = to_delete.right
    # to_delete is right child
    else:
      prev.right = to_delete.right
  # node to delete has left child
  elif to_delete.right is None:
    # delete root
    if to_delete is root:
      root = to_delete.left
    # to_delete is left child
    elif prev.left is to_delete:
      prev.left = to_delete.left
    # to_delete is right child
    else:
      prev.right = to_delete.left
  # 2 child case
  else:
    successor = findNextIter(root, to_delete.val)
    if to_delete is root:
      root = successor
    # to_delete is left child
    elif prev.left is to_delete:
      prev.left = successor
    # to_delete is right child
    else:
      prev.right = successor
    successor.left = to_delete.left
    
# next/prev will return node rather than val because i need the node for deletion
def findNextIter(root, val):
  cursor = root
  while cursor is not None:
    if cursor.val == val and root.left:
      return findMaxIter(cursor.left)
    elif cursor.val < val:
      cursor = cursor.right
    else:
      cursor = cursor.left
  return cursor

def findPrevIter(root, val):
  cursor = root
  while cursor is not None:
    if cursor.val == val and root.right:
      return findMinIter(cursor.right)
    elif cursor.val < val:
      cursor = cursor.right
    else:
      cursor = cursor.left
  return cursor

def findMinIter(root):
  cursor = root
  while cursor.left is not None:
    cursor = cursor.left
  return cursor.val

def findMaxIter(root):
  cursor = root
  while cursor.right is not None:
    cursor = cursor.right
  return cursor.val