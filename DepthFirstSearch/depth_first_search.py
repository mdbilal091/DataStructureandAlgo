"""Here we need to write an actual depth first logic"""

from helper import get_path,is_legal_position,offset, read_maze
from stack import Stack

def dfs(maze,start,goal):

    s = Stack()
    s.push(start)
    predecessors = {start: None}

    while not s.is_empty():
        cur_cell = s.pop()
        if cur_cell == goal:
            return get_path(predecessors,start,goal)
        for dirc in ["up","right","down","left"]:
            row_offset, col_offset = offset[dirc]
            neighbour = (cur_cell[0] + row_offset, cur_cell[1]+col_offset)
            if is_legal_position(maze,neighbour) and neighbour not in predecessors:
                s.push(neighbour)
                predecessors[neighbour] = cur_cell
    return None


if __name__ == "__main__":
    """maze = [[0]*4 for row in range(4)]
    start_pos = (0,0)
    goal_pos = (2,3)
    result = dfs(maze,start_pos,goal_pos)
    print(result)"""

    #Challenge

    maze1 = read_maze("/Users/bilalmohammed 1/Documents/GitHub/DataStructureandAlgo/mazefile/dfs_challenge.txt")
    for row in maze1:
        print(row)
    start_pos1 = (1,1)
    goal_pos1 = (2,4)
    result1 = dfs(maze1,start_pos1,goal_pos1)
    print(result1)