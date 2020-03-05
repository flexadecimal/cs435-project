class bst_node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  def __repr__(self):
    return str(self.val)

class bst:
  def __init__(self):
    self.root = None

  def insertIter(self, val):
    # base case - empty tree
    if self.root is None:
      self.root = bst_node(val)
      return
    # search for node
    cursor = self.root
    prev = None
    while cursor is not None:
      prev = cursor
      cursor = cursor.left if val <= cursor.val else cursor.right
    cursor = bst_node(val)
    if val < prev.val:
      prev.left = cursor
    else:
      prev.right = cursor

  def deleteIter(self, val):
    # search for note to delete and keep track of parent
    # root case
    if self.root.val == val:
      to_del = self.root
    else:
      cursor = self.root
      prev = None
      parent = None
      # find node to delete, and parent
      while cursor is not None:
        parent = prev
        prev = cursor
        cursor = cursor.left if val <= cursor.val else cursor.right
      to_del = prev
    # leaf case
    if to_del.left is None and to_del.right is None:
      # root subcase
      if to_del is self.root:
        self.root = None
      # set left or right of parent to null accordingly
      elif parent.left is to_del:
        parent.left = None
      else:
        parent.right = None
    # 1 child case
    elif to_del.left is None or to_del.right is None:
      child = to_del.left if to_del.left else to_del.right
      # root case
      if to_del is self.root:
        self.root = child
      # child of root subcase - just skip over
      elif parent is self.root:
        if to_del is self.root.left:
          self.root.left = child
        else:
          self.root.right = child
      # child of deleted adopted by parent
      elif parent.left is to_del:
        to_del.left = child
      else:
        to_del.right = child
    # 2 child case
    else:
      # get successor
      successor = self.findNextIter(to_del)
      # root subcase
      if to_del == self.root:
        new_root = self.root.left
        self.root = new_root
        new_root.right = successor
      # oprhaned successor in node to delete's place
      elif parent.left is cursor:
        to_del.parent.left = successor
      else:
        to_del.parent.right = successor
        
  # the following are the same as bst because avl trees are subset of bst
  def findNextIter(self, node):
    cursor = self.root
    while cursor is not None:
      if cursor.val == node.val and self.root.left:
        return self.findMaxIter(cursor.left)
      cursor = cursor.left if node.val <= cursor.val else cursor.right
    return cursor
    
  def findPrevIter(self, node):
    cursor = self.root
    while cursor is not None:
      if cursor.val == node.val and self.root.right:
        return findMinIter(cursor.right)
      cursor = cursor.left if node.val <= cursor.val else cursor.right
    return cursor
    
  def findMinIter(self, node):
    cursor = self.root
    while cursor.left is not None:
      cursor = cursor.left
    return cursor
    
  def findMaxIter(self, node):
    cursor = self.root
    while cursor.right is not None:
      cursor = cursor.right
    return cursor

# for testing
if __name__ == "__main__":
  vals = [44, 33, 2, 43, 12, 5, 80, 67]
  tree = bst()
  for n in vals:
    tree.insertIter(n)
  for n in reversed(vals):
    tree.deleteIter(n)
  pass