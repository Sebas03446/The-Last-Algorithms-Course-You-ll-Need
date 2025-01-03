from tree.tree import BinaryNode

class BreadthFirstSearch:
    def __init__(self):
        pass
    
    def bfs(self, head: BinaryNode, num: int) -> bool:
        queue = [head]
        
        while queue:
            current = queue.pop(0)
            
            if current.v == num:
                return True
            
            if current.l:
                queue.append(current.l)
            if current.r:
                queue.append(current.r)
        
        return False
    