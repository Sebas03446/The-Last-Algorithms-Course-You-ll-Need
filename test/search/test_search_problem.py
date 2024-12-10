import pytest
import random
from search import search_problem

def test_two_crystal_balls_problem():
    breaks = [False,True,True,True,True,True,True,True]

    assert search_problem.SearchProblem.two_crystal_problem(breaks) == 1

def test_two_crystal_balls_problem_random():
    idx = random.randint(0,10000)
    data = [False]*10000
    for i in range(idx,10000):
        data[i] = True
    assert search_problem.SearchProblem.two_crystal_problem(data) == idx
