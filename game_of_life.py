import random
import time
import os

DEAD = 0
ALIVE = 1


def random_state(height, width):

    # Generate a random board state by using a list comprehension to generate a list of random 0 or 1 values
    # threshold == 0.5
    board_state = [[round(random.random()) for _ in range(width)]
                   for _ in range(height)]

    # Return the random board state
    return board_state


def dead_state(height, width):

    # Create an empty list to store the board state
    board_state = list()

    # Iterate over the rows of the board
    for i in range(height):
        # Append an empty list to the board state to represent a new row
        board_state.append([])

        # Iterate over the columns of the board
        for _ in range(width):
            # Append a 0 to the current row to represent a dead cell
            board_state[i].append(DEAD)

    # Return the board state
    return board_state


def render(board_state):

    os.system("clear")
    # Get the width of the board by taking the length of the first row
    width = len(board_state[0])

    # Create the top and bottom border using the width of the board
    # multiplied by 2 to account for the spaces inbetween,
    # plus three extra characters for the spaces and border characters
    topbottom_border = '-' * (width * 2 + 3)

    # Print the border
    print(topbottom_border)

    # Iterate over the rows of the board
    for row in board_state:
        print('|', end=' ')
        for cell in row:
            if cell:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print('|')

    # Print the border again to complete the visual representation of the board
    print(topbottom_border)


def next_board_state(initial_state):

    height = len(initial_state)
    width = len(initial_state[0])
    new_state = dead_state(height, width)

    for i in range(height):
        for j in range(width):
            alive_neighbours = 0
            # Top-left corner
            if i == 0 and j == 0:
                alive_neighbours = initial_state[i][j+1] + \
                    initial_state[i+1][j+1] + initial_state[i+1][j]

            # Top-right corner
            elif i == 0 and j == width-1:
                alive_neighbours = initial_state[i+1][j] + \
                    initial_state[i+1][j-1] + initial_state[i][j-1]

            # Top row except corners
            elif i == 0:
                alive_neighbours = initial_state[i][j+1] + initial_state[i+1][j+1] + \
                    initial_state[i+1][j] + initial_state[i +
                                                          1][j-1] + initial_state[i][j-1]

            # Bottom-left corner
            elif i == height-1 and j == 0:
                alive_neighbours = initial_state[i-1][j] + \
                    initial_state[i-1][j+1] + initial_state[i][j+1]

            # Bottom-right corner
            elif i == height-1 and j == width-1:
                alive_neighbours = initial_state[i][j-1] + \
                    initial_state[i-1][j-1] + initial_state[i-1][j]

            # Bottom row except corners
            elif i == height-1:
                alive_neighbours = initial_state[i][j-1] + initial_state[i-1][j-1] + \
                    initial_state[i-1][j] + initial_state[i -
                                                          1][j+1] + initial_state[i][j+1]

            # Most-left column
            elif j == 0:
                alive_neighbours = initial_state[i-1][j] + initial_state[i-1][j+1] + \
                    initial_state[i][j+1] + initial_state[i +
                                                          1][j+1] + initial_state[i+1][j]

            # Most-right column
            elif j == width-1:
                alive_neighbours = initial_state[i+1][j] + initial_state[i+1][j-1] + \
                    initial_state[i][j-1] + initial_state[i -
                                                          1][j-1] + initial_state[i-1][j]

            # Everywhere else
            else:
                alive_neighbours = initial_state[i-1][j] + initial_state[i-1][j+1] + initial_state[i][j+1] + initial_state[i+1][j+1] + initial_state[i+1][j] \
                    + initial_state[i+1][j-1] + \
                    initial_state[i][j-1] + initial_state[i-1][j-1]

            cell = initial_state[i][j]
            if cell == ALIVE:
                if alive_neighbours == 0 or alive_neighbours == 1:
                    new_state[i][j] = DEAD
                elif alive_neighbours > 3:
                    new_state[i][j] = DEAD
                else:
                    new_state[i][j] = ALIVE
            else:
                if alive_neighbours == 3:
                    new_state[i][j] = ALIVE

    return new_state


def main():

    height = 30
    width = 50
    board_state = random_state(height, width)
    render(board_state)
    while True:
        board_state = next_board_state(board_state)
        render(board_state)
        time.sleep(0.4)


main()
