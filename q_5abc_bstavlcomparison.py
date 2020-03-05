from q_1c_bstrec_code import bst as bst_rec
from q_1d_bstiter_code import bst as bst_iter
from q_4a_avliter_code import avl_tree as avl_tree_iter
from q_3ab_code import getRandomArray, getSortedArray

if __name__ == "__main__":
  random_10 = getRandomArray(10)
  random_10k = getRandomArray(10000)
  print("5a. Constructing bst:recursive, avl:iterative trees of size 10,000... (random)")
  bst_10k = bst_rec()
  avl_10k = avl_tree_iter()
  for n in random_10k:
    bst_10k.insertRec(n)
    avl_10k.insertIter(n)
  print("5b. Constructing bst:recursive, avl:iterative trees of size 10 (random)")
  bst_10rec = bst_rec()
  avl_10 = avl_tree_iter()
  for n in random_10k:
    bst_10rec.insertRec(n)
    avl_10.insertIter(n)
  print("5c. Constructing bst:iterative, avl:iterativetrees of size 10,000 (random)")
  bst_10iter = bst_iter()
  avl_10c = avl_tree_iter()
  for n in random_10k:
    bst_10iter.insertIter(n)
    avl_10c.insertIter(n)