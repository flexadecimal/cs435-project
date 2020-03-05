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

  def insertRec(self, val):
    def helper(root, val):
      node = bst_node(val)
      if root is None:
        self.root = node
        return;
      elif val < root.val:
        if root.left is None:
          root.left = node
        else:
          helper(root.left, val)
      else:
        if root.right is None:
          root.right = node
        else:
          helper(root.right, val)
    helper(self.root, val)

  def deleteRec(self, val):
    # this returns the new root
    def helper(root, val):
      # base case
      if root is None:
        return root
      if val < root.val:
        root.left = helper(root.left, val)
      elif val > root.val:
        root.right = helper(root.right, val)
      # found node to be deleted
      else:
        # root case
        if root is self.root:
          self.root = None
          return
        # 0/1 child case
        elif root.left is None:
          return root.right
        elif root.right is None:
          return root.left
        # 2 child case
        else:
          temp = self.findPrevRec(root.right)
          root.val = temp.val
          root.right = helper(root.right, temp.val)
      return root
    helper(self.root, val)
  
  def findNextRec(self, node):
    def helper(root, node):
      if root is None:
        return None
      if root.val == node.val:
        return self.findMinRec(root.right)
      elif root.val < node.val:
        return helper(root.left, node)
      else:
        return helper(root.right, node)
    return helper(node)

  def findPrevRec(self, node):
    def helper(root, val):
      if root is None:
        return None
      if root.val == node.val:
        return self.findMaxRec(root.left)
      elif root.val < node.val:
        return helper(root.left, node)
      else:
        return helper(root.right, node)
    return helper(node)
  
  def findMinRec(self):
    def helper(root):
      if root.left is None:
        return root
      else:
        return helper(root.left)
    return helper(self.root)

  def findMaxRec(self):
    def helper(root):
      if root.right is None:
        return root
      else:
        return helper(root.right)
    return helper(self.root)
    
# for testing
if __name__ == "__main__":
  vals = [44, 33, 2, 43, 12, 5, 80, 67]
  tree = bst()
  for n in vals:
    tree.insertRec(n)
  for n in reversed(vals):
    tree.deleteRec(n)
  pass