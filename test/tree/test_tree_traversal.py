from tree.tree_traversal import PreOrder, InOrder, PostOrder
from test.tree.sample_tree import get_sample_tree

tree = get_sample_tree()

def test_pre_order_tree_traversal():
    print(tree.root,tree.root.v)
    assert PreOrder().pre_order_search(tree.root) == [20,10,5,7,15,50,30,29,45,100]
    
def test_in_order_tree_traversal():
    assert InOrder().in_order_search(tree.root) == [5,7,10,15,20,29,30,45,50,100]

def test_post_order_tree_traversal():
    assert PostOrder().post_order_search(tree.root) == [7,5,15,10,29,45,30,100,50,20]