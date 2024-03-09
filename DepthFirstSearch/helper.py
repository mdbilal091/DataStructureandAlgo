"""Creating some helper function to use in Depth First Search"""

offset = {
    "right":(0,1),
    "left":(0,-1),
    "up":(-1,0),
    "down":(1,0)
}

""" Reading maze from file"""

def read_maze(filename):
    try:
        with open(filename) as fn:
            maze = []
            for lines in fn:
                row = []
                for char in lines.strip("\n"):
                    row.append(char)
                maze.append(row)
            num_colum_in_row = len(maze[0])
            for row in maze:
                if len(row) != num_colum_in_row:
                    print("The Maze is not rectangular")
                    raise SystemExit
            return maze
    except IOError:
        print("File is Corrupted")
        raise SystemExit


"""This function check the position is legal which means it exist in the maze and not an obstacle"""

def is_legal_position (maze,pos):
    i,j = pos
    no_row = len(maze)
    no_column = len(maze[0])
    if 0 <= i < no_row and 0 <= j < no_column and maze[i][j] != "*":
        return True
    else:
        return False

"""This function is used to get the paths """

def get_path(predecessors, start, goal):
    current_pos = goal
    path = []
    while current_pos != start:
        path.append(current_pos)
        current_pos = predecessors[current_pos]
    path.append(start)
    path.reverse()
    return path

