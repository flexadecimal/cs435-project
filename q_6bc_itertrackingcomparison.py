from q_6a_avliter_tracking import avl_tree
from q_6a_bstiter_tracking import bst
from q_3ab_code import getRandomArray, getSortedArray

if __name__ == "__main__":
  random_10k = getRandomArray(10000)
  print("6ab. Constructing bst:iterative, avl:iterative trees of size 10,000... (random)")
  bst_10k = bst()
  avl_10k = avl_tree()
  for n in random_10k:
    bst_10k.insertIter(n)
    avl_10k.insertIter(n)
  print("\tbst levels traversed: {}, avl levels traversed: {}".format(bst_10k.lvl_counter, avl_10k.lvl_counter))
  sorted_10k = getSortedArray(10000)
  print("6c. Constructing bst:iterative, avl:iterative trees of size 10,000... (sorted)")
  bst_10k_sorted = bst()
  avl_10k_sorted = avl_tree()
  for n in sorted_10k:
    bst_10k_sorted.insertIter(n)
    avl_10k_sorted.insertIter(n)
  print("\tbst levels traversed: {}, avl levels traversed: {}".format(bst_10k_sorted.lvl_counter, avl_10k_sorted.lvl_counter))
  
