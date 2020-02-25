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

def deleteRec(root, val):
  if root is None:
    return root
  if val < root.val:
    root.left = deleteRec(root.left, val)
  elif val > root.val:
    root.right = deleteRec(root.right, val)
  else:
    if root.left is None:
      temp = root.right
      del(root)
      return temp
    elif root.right is None:
      temp = root.left
      del(root)
      return temp
    temp = findPrevRec(root.right)
    root.val = temp
    root.right = deleteRec(root.right, temp)
  return root

def findNextRec(root, val):
  if root is None:
    return
  if root.val == val:
    return findMinRec(root.right)
  elif root.val < val:
    return findNextRec(root.left, val)
  else:
    return findNextRec(root.right, val)

def findPrevRec(root, val):
  if root is None:
    return
  if root.val == val:
    return findMaxRec(root.left)
  elif root.val < val:
    return findPrevRec(root.left, val)
  else:
    return findPrevRec(root.right, val)

def findMinRec(root):
  if root.left is None:
    return root.val
  else:
    return findMinRec(root.left)

def findMaxRec(root):
  if root.right is None:
    return root.val
  else:
    return findMaxRec(root.right)