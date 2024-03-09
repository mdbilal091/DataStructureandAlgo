
"""Here we are writing the actual breadth First Search algorithm Function using QUEUE Data Structure"""
from queue_learn import Queue
from DepthFirstSearch.helper import get_path, offset, is_legal_position, read_maze

def bfs(maze, start, end):

    q = Queue()
    predecessor = {start: None}
    q.enqueue(start)

    while not q.is_empty():
        current_position = q.dequeue()
        if current_position == end:
            print(get_path(predecessor,start,end))
            return get_path(predecessor,start, end)
        for direction in ["up","right","down", "left"]:
            row_offset, column_offset = offset[direction]
            neighbour = (current_position[0] + row_offset, current_position[1] + column_offset)
            if is_legal_position(maze, neighbour) and neighbour not in predecessor:
                q.enqueue(neighbour)
                predecessor[neighbour] = current_position
    return None

if __name__ == "__main__":

    maze1 = read_maze("/Users/bilalmohammed 1/Documents/GitHub/DataStructureandAlgo/mazefile/dfs_challenge.txt")
    #for row in maze1:
        #print(row)
    start_pos1 = (1, 1)
    goal_pos1 = (2, 4)
    result1 = bfs(maze1, start_pos1, goal_pos1)
    #print(result1)