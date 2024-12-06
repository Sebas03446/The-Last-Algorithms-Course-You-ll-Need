#First question: Is it ordered?
# Yes, we don't need to start from the beginning, we can start from the middle
import math

class BinarySearch:
    def __init__(self):
        pass

def binary_search( list, target):
    
    lo = 0
    hi = len(list) -1
    
    return search(list,lo,hi,target)

def search(list, lo, hi, t):
    if lo > hi:
        return False
    
    m = math.floor(lo + (hi-lo)/2)
    
    val = list[m]
    
    if val == t:
        return True
    elif t > val:
        lo = m +1
        return search(list,lo, hi,t)
    else:
        hi = m -1
        return search(list, lo,hi,t)