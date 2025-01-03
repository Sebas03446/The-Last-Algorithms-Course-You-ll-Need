import math

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val: int):
        self.heap.append(val)
        self.heapifyUp(len(self.heap)-1)
    
    
    def delete(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        
        return root
    
    def heapifyDown(self,idx):
        l_idx = self.leftChild(idx)
        r_idx = self.rightChild(idx)
        
        if idx >= len(self.heap) or l_idx >= len(self.heap) or r_idx >= len(self.heap):
            return
        
        l_v = self.heap[l_idx]
        r_v = self.heap[r_idx]
        v = self.heap[idx]
        
        if l_v > r_v and v > r_v:
            self.heap[r_idx] = v
            self.heap[idx] = r_v
            self.heapifyDown(r_idx)
        elif l_v < r_v and v > l_v:
            self.heap[l_idx] = v
            self.heap[idx] = l_v
            self.heapifyDown(l_idx)
            
    def heapifyUp(self, idx):
        if idx == 0:
            return
        
        p = self.parent(idx)
        
        parent_v = self.heap[p]
        v = self.heap[idx]
        
        if parent_v > v:
            self.heap[p]= v
            self.heap[idx] = parent_v
            
            self.heapifyUp(p)
    
    def parent(self, idx):
        return math.floor((idx - 1)/2)
    
    def leftChild(self, idx):
        return idx*2+1
    
    def rightChild(self, idx):
        return idx*2+2