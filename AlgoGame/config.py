"""
Python Data Structures Practice - A Fun Game-Based Approach
"""

BOARD_FILE = "game_boards/pacman_board.txt"
#BOARD_FILE = "game_boards/wide_board.txt"
#BOARD_FILE = "game_boards/walled_garden_10x10.txt"

PLAYER = "P"
OPPONENT = "O"
OBSTACLE = "*"
GAME_SPEED = 100
TARGET_SCORE = 3
WIDTH = 1200
HEIGHT = 740
BUTTON_FONT = ('Arial', 12, 'normal')
SCORE_FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 18, "normal")
SOUND = True

offset_parameter = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}