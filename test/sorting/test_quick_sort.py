from sorting.quick_sort import QuickSort

def test_quick_sort():
    arr_ = [9,3,7,4,68,500,42]
    QuickSort().sort(arr_)
   
    assert arr_ == [3,4,7,9,42,68,500]
       