import sorting.bubble_sort as bubble_sort

def test_bubble_sort():
    nums = [5, 3, 8, 6, 2]
    bubble = bubble_sort.BubbleSort()
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 8]
    
    nums = [5, 3, 8, 6, 2, 7]
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 7, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7]
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 7, 8, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7, 7]
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 7, 7, 8, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7, 7, 7]
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 7, 7, 7, 8, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7, 7, 7, 7]
    bubble.sort(nums)
    assert nums == [2, 3, 5, 6, 7, 7, 7, 7, 8, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7, 7, 7, 7, 1]
    bubble.sort(nums)
    assert nums == [1, 2, 3, 5, 6, 7, 7, 7, 7, 8, 8]
    
    nums = [5, 3, 8, 8, 6, 2, 7, 7, 7, 7, 1, 4]
    bubble.sort(nums)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 8]