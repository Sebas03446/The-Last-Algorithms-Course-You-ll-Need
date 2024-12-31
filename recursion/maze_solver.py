

class MazeSolver:
    def __init__(self, maze, wall, start, end):
        self.maze = maze
        self.wall = wall
        self.start = start
        self.end = end

    def solve(self):
        return maze_solver(self.maze, self.wall, self.start, self.end)

dir = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]
def walk(maze,wall,current, end, seen, path):
    if current['x'] <0 or current['x'] >= len(maze[0] or current['y']<0 or current['y'] <= len(maze) ):
        return False
    
    if maze[current['y']][current['x']] == wall:
        return False
    
    if current['x'] ==  end['x'] and current['y'] == end['y']:
        path.append(end)
        return True
    
    
    if seen[current['y']][current['x']]:
        return False
    
    seen[current['y']][current['x']] = True
    path.append(current)
    
    for i in dir:
        y = i[0]
        x = i[1]
        if(walk(maze, wall, {'x': current['x'] + x, 'y': current['y'] + y}, end, seen, path)):
            return True
        
    
    path.pop()
    
    return False    

def maze_solver(maze, wall, current, end):
    seen = [[False for i in range(len(maze[0]))] for i in range(len(maze))]
    path = []
    
    walk(maze,wall, current, end, seen, path)
    
    return path
    
    