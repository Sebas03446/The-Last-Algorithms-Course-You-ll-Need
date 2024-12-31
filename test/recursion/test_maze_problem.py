import pytest
from recursion import maze_solver
from recursion.maze_solver import MazeSolver

def draw_path(data, path):
    data2 = [list(row) for row in data]
    for p in path:
        if data2[p['y']] and data2[p['y']][p['x']]:
            data2[p['y']][p['x']] = '*'
    return [''.join(d) for d in data2]

def test_maze_solver():
    maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]

    maze_result = [
        {'x': 10, 'y': 0},
        {'x': 10, 'y': 1},
        {'x': 10, 'y': 2},
        {'x': 10, 'y': 3},
        {'x': 10, 'y': 4},
        {'x': 9, 'y': 4},
        {'x': 8, 'y': 4},
        {'x': 7, 'y': 4},
        {'x': 6, 'y': 4},
        {'x': 5, 'y': 4},
        {'x': 4, 'y': 4},
        {'x': 3, 'y': 4},
        {'x': 2, 'y': 4},
        {'x': 1, 'y': 4},
        {'x': 1, 'y': 5},
    ]

    # There is only one path through
    solver = MazeSolver(maze, "x", {'x': 10, 'y': 0}, {'x': 1, 'y': 5})
    result = solver.solve()
    assert draw_path(maze, result) == draw_path(maze, maze_result)