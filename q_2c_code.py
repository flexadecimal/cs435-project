from q_1c_bstrec_code import bst

def inorder(root):
  out = []
  def helper(root):
    if root:
      helper(root.left)
      out.append(root.val)
      helper(root.right)
  helper(root)
  return out
    
def bst_sort(unsorted):
  tree = bst()
  for val in unsorted:
    tree.insertRec(val)
  return inorder(tree.root)

# for testing
if __name__ == "__main__":
  vals = [10, 5, 6, 7, 20, 12, 11, 16, 19, 18, 17]
  tree = bst()
  for n in vals:
    tree.insertRec(n)
  print(inorder(tree.root))