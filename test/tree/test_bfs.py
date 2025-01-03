from tree.bfs import BreadthFirstSearch
from test.tree.sample_tree import get_sample_tree

tree = get_sample_tree()

def test_bfs():
    assert BreadthFirstSearch().bfs(tree.root, 100) == True
    assert BreadthFirstSearch().bfs(tree.root, 20) == True
    assert BreadthFirstSearch().bfs(tree.root, 7) == True
    assert BreadthFirstSearch().bfs(tree.root, 200) == False