from heap.min_heap import MinHeap

def test_min_heap():
    heap = MinHeap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(15)
    heap.insert(30)
    heap.insert(5)
    heap.insert(100)
    heap.insert(45)
    heap.insert(7)
    heap.insert(50)
    heap.insert( 29)
    assert heap.delete() == 5