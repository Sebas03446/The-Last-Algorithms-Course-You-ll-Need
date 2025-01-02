from tree.tree import BinaryNode

class PreOrder:
    def __init__(self):
        pass
    
    def walk(self, curr: BinaryNode ,path: list):
        if not curr :
            return
        
        path.append(curr.v)
        
        self.walk(curr.l,path)
        self.walk(curr.r,path)
    
    def pre_order_search(self, head):
        path = []
        self.walk(head, path)
        return path
    

class InOrder:
    def __init__(self):
        pass
    
    def walk(self, curr: BinaryNode ,path: list):
        if not curr :
            return
        
        self.walk(curr.l,path)
        path.append(curr.v)
        self.walk(curr.r,path)
    
    def in_order_search(self, head):
        path = []
        self.walk(head, path)
        return path

class PostOrder:
    def __init__(self):
        pass
    
    def walk(self, curr: BinaryNode ,path: list):
        if not curr :
            return
        
        self.walk(curr.l,path)
        self.walk(curr.r,path)
        path.append(curr.v)
    
    def post_order_search(self, head):
        path = []
        self.walk(head, path)
        return path
