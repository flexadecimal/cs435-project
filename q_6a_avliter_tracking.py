class avl_node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    # parent reference needed for updating height/bf backtracking
    self.parent = None
    self.bf = 0
    self.height = -1
  def __repr__(self):
    return str(self.val)
  
# need to keep reference to root node
class avl_tree:
  def __init__(self):
    self.root = None
    self.lvl_counter = 0
   
  # insert/delete util functions: rotations. see lesson 9 slides for details. these update height/bf as well!
  def __r_rotate(self, node):
    a = node
    b = a.left
    s2 = b.right
    # rotation - s2 goes under a...
    a.left = s2
    if s2 is not None:
      s2.parent = a
    # ...b's parent is now a's parent (b and a switch places)...
    b.parent = a.parent
    # handling edge case: rotating on root
    if a.parent is None:
      self.root = b
    # modify parent
    elif a is a.parent.right:
      a.parent.right = b
    else:
      a.parent.left = b
    # ... b goes under a
    b.right = a
    a.parent = b
    # update a then b
    self.__update_hbf(a)
    self.__update_hbf(b)

  def __l_rotate(self, node):
    b = node
    a = b.right
    s2 = a.left
    # rotation - s2 goes under b...
    b.right = s2
    if s2 is not None:
      s2.parent = b
    # ...swap parents like above...
    a.parent = b.parent
    # handle rotate on root like above
    if b.parent is None:
      self.root = a
    # modify parent
    elif b == b.parent.left:
      b.parent.left = a
    else:
      b.parent.right = a
    # ... b goes under a
    a.left = b
    b.parent = a
    # update b then a
    self.__update_hbf(b)
    self.__update_hbf(a)
  # update height and bf, used upon insertion
  def __update_hbf(self, node):
    if node.left is None:
      l_height = -1
    else:
      l_height = node.left.height
    if node.right is None:
      r_height = -1
    else:
      r_height = node.right.height
    # set bf
    node.bf = l_height - r_height
    node.height = 1 + max(l_height, r_height)
  # backtrack and do rotations
  def __rebalance(self, node):
    cursor = node
    prev = node.parent
    # backtrack and update, including root
    while cursor is not None:
      self.__update_hbf(cursor)
      # now do rotations
      self.__update_hbf(node)
      if cursor.bf > 1:
        if cursor.left.bf < 0:
          # lr case, rotate left first
          self.__l_rotate(cursor.left)
        # ll case
        self.__r_rotate(cursor)
      elif cursor.bf < -1:
        if cursor.right.bf > 0:
          #rl case, rotate right first
          self.__r_rotate(cursor.right)
        # rr case
        self.__l_rotate(cursor)
      prev = cursor
      cursor = cursor.parent
      self.lvl_counter += 1
  
  def insertIter(self, val):
    # base case - empty tree
    if self.root is None:
      self.root = avl_node(val)
      self.__rebalance(self.root)
      return
    # same as bst - find empty leaf
    cursor = self.root
    prev = None
    while cursor is not None:
      prev = cursor
      cursor = cursor.left if val <= cursor.val else cursor.right
      self.lvl_counter += 1
    # the empty cursor is now a node
    cursor = avl_node(val)
    if val < prev.val:
      # insert into left
      prev.left = cursor
    else:
      # insert into right
      prev.right = cursor
    # set new node parent (used for backtracking)
    cursor.parent = prev
    # update and rebalance if needed - backtrack from cursor
    self.__rebalance(cursor)
  # doesn't check for nonexistent value. only give valid values pls
  def deleteIter(self, val):
    # root case
    if self.root.val == val:
      to_del = self.root
    else:
      # binary search for node to delete
      cursor = self.root
      prev = None
      while cursor is not None:
        prev = cursor
        cursor = cursor.left if val <= cursor.val else cursor.right
        self.lvl_counter += 1
      to_del = prev
    # no children i.e. leaf case
    if to_del.left is None and to_del.right is None:
      # root subcase
      if to_del is self.root:
        self.root = None
      # set left or right of parent to null accordingly
      elif to_del.parent.left is to_del:
        to_del.parent.left = None
      else:
        to_del.parent.right = None
    # 1 child case
    elif to_del.left is None or to_del.right is None:
      child = to_del.left if to_del.left else to_del.right
      # root case
      if to_del is self.root:
        self.root = child
      # child of root subcase - just skip over
      elif to_del.parent is self.root:
        if to_del is self.root.left:
          self.root.left = child
        else:
          self.root.right = child
        child.parent = self.root
      # child of deleted adopted by parent
      elif to_del.parent.left is to_del:
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
        successor.parent = new_root
      # oprhaned successor in node to delete's place
      elif to_del.parent.left is cursor:
        successor.parent.left = None
        to_del.parent.left = successor
      else:
        successor.parent.right = None
        to_del.parent.right = successor
    # now rebalance
    self.__rebalance(to_del)
    
  # the following are the same as bst because avl trees are subset of bst
  def findNextIter(self, node):
    cursor = self.root
    while cursor is not None:
      if cursor.val == node.val and self.root.left:
        return self.findMaxIter(cursor.left)
      cursor = cursor.left if node.val <= cursor.val else cursor.right
      self.lvl_counter += 1
    return cursor
  
  def findPrevIter(self, node):
    cursor = self.root
    while cursor is not None:
      if cursor.val == node.val and self.root.right:
        return findMinIter(cursor.right)
      cursor = cursor.left if node.val <= cursor.val else cursor.right
      self.lvl_counter += 1
    return cursor
  
  def findMinIter(self, node):
    cursor = self.root
    while cursor.left is not None:
      cursor = cursor.left
      self.lvl_counter += 1
    return cursor
  
  def findMaxIter(self, node):
    cursor = self.root
    while cursor.right is not None:
      cursor = cursor.right
      self.lvl_counter += 1
    return cursor

# for testing
if __name__ == "__main__":
  vals = [2, 4, 54, 12, 43, 5, 13, 6, 88]
  tree = avl_tree()
  for n in vals:
    tree.insertIter(n)
  for n in reversed(vals):
    tree.deleteIter(n)
  pass