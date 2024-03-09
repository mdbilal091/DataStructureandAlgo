"""Reading challenge file to create maze using 2D list"""

def read_maze(filename):
#Using try except block to catch any errors
    try:
        #Opening files
        with open(filename) as fn:
            #defining empty maze
            maze = []
            #reading lines from file
            for line in fn:
                #defining empty rows
                row = []
                for char in line.strip("\n"):
                    row.append(char)
                maze.append(row)
            num_col_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_col_top_row:
                    print("Maze is not Rectangular")
                    raise SystemExit
            return maze
    except OSError:
        print("Problem is with the input file")
        raise SystemExit

if __name__ == "__main__":
    maze = read_maze('/Users/bilalmohammed 1/Documents/GitHub/DataStructureandAlgo/mazefile/challenge.txt')
    for row in maze:
        print(row)