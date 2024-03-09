"""
Python Data Structures Practice - A Fun Game-Based Approach
Helper functions to use in Graphical User Interface.
"""
import config


def screen_coordinates_from_grid_position(position, grid_dimensions):
    """
    Converts grid-based coordinates to screen based coordinates.
    """
    i, j = position
    screen_x = - ((grid_dimensions[1] - 1) / 2 * 20) + (j * 20)
    screen_y = ((grid_dimensions[0] - 1) / 2 * 20) - (i * 20)
    return (screen_x, screen_y)


def grid_position_from_screen_coordinates(position, dimensions):
    """
    Converts screen-based coordinates to grid-based coordinates.
    """
    x, y = position
    m, n = dimensions
    j = int((20 * (n / 2) + x) / 20)
    i = int((20 * (m / 2) - y) / 20)
    return (i, j)


def read_board_from_file(filename):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(filename) as fn:
            # Convert string maze to 2d list
            maze = [[char for char in line.strip("\n")] for line in fn]

            # Get board dimensions
            top_row_columns_numbers = len(maze[0])
            rows_number = len(maze)

            # Check if the board is rectangular
            for row in maze:
                if len(row) != top_row_columns_numbers:
                    print("The maze is not rectangular.")
                    raise SystemExit

            # Find obstacles and initial positions for player and opponent
            maze_obstacles = []
            for i in range(rows_number):
                for j in range(top_row_columns_numbers):
                    if maze[i][j] == config.OBSTACLE:
                        maze_obstacles.append((i, j))
                    elif maze[i][j] == config.PLAYER:
                        player_start_pos = (i, j)
                    elif maze[i][j] == config.OPPONENT:
                        opponent_start_pos = (i, j)

            return maze, (rows_number, top_row_columns_numbers), maze_obstacles, player_start_pos, opponent_start_pos
    except UnboundLocalError:
        print("The maze needs a player and an opponent.")
        raise SystemExit
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def is_legal_position(board, position):
    """
    Determines whether a supplied position is legal in the context of a supplied board.
    """
    i, j = position
    num_rows = len(board)
    num_cols = len(board[0])
    if 0 <= i < num_rows and 0 <= j < num_cols and board[i][j] != config.OBSTACLE:
        return True
    else:
        return False
