# Given two crystal balls that will break if dropped from high enough
# distance, determine the exact spot in which it will break in the most
# optimized way.

import math

class SearchProblem:
    def __init__(self):
        pass
    def two_crystal_problem(breaks):
        jump_steps = math.floor(math.sqrt(len(breaks)))
        
        i = jump_steps
        while(i<len(breaks)):
            if(breaks[i]):
                break
            
            i+=jump_steps
        
        i-=jump_steps
        for j in range(i,i+jump_steps):
            if(breaks[j]):
                return j
            
        return -1