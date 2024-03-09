
"""Here are the a-star algorithm logic"""
from priorityqueue import priorityqueue
from DepthFirstSearch.helper import get_path, offset, is_legal_position, read_maze

def heuristic(a,b):
    """"Calculate the manhaten distance between two pair of grid coordinates"""

    x1,y1 = a
    x2,y2 = b

    return abs(x1-x2) + abs(y1-y2)

def astar(maze, start, goal):

    pq1 = priorityqueue()
    pq1.put(start, 0)
    predecessor = {start: None}
    g_value = {start: 0}

    while not pq1.is_empty():
        current_cell = pq1.get()
        if current_cell == goal:
            return get_path(predecessor, start, goal)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offset[direction]
            neighbour = (current_cell[0]+row_offset,current_cell[1]+col_offset)

            if is_legal_position(maze, neighbour) and neighbour not in g_value:
                new_cost = g_value[current_cell] + 1
                g_value[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq1.put(neighbour, f_value)
                predecessor[neighbour] = current_cell

    return None


if __name__ == "__main__":

    maze1 = read_maze("/Users/bilalmohammed 1/Documents/GitHub/DataStructureandAlgo/mazefile/astar_challenge")
    for row in maze1:
        print(row)
    start_pos1 = (1,0)
    goal_pos1 = (4,4)
    result1 = astar(maze1,start_pos1,goal_pos1)
    print(result1)



