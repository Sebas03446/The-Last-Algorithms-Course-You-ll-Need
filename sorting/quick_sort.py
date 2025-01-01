

class QuickSort:
    def __init__(self):
        pass
    
    def sort(self, arr):
        qs(arr,0,len(arr)-1)
    

def qs(arr, lo, hi):
    if lo >= hi:
        return
    
    pivot_idx = partition(arr,lo,hi)
    
    qs(arr,lo,pivot_idx-1)
    qs(arr,pivot_idx+1,hi)

def partition(arr,lo,hi): 
    pivot = arr[hi]
    
    idx= lo - 1 
    
    for i in range(lo,hi): 
        if arr[i]<= pivot: 
            idx+=1  
            tmp= arr[i] 
            arr[i] = arr[idx]
            arr[idx]=tmp
    
    idx+=1
    arr[hi]=arr[idx]
    arr[idx]= pivot
    
    return idx
    