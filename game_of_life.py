import random

def random_state(height, width):
    # Create a dead board state using the dead_state function
    board_state = dead_state(height, width)


    # Generate a random board state by using a list comprehension to generate a list of random 0 or 1 values
    # threshold == 0.5
    board_state = [[round(random.random()) for _ in range(height)] for _ in range(width)]

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
        for j in range(width):
            # Append a 0 to the current row to represent a dead cell
            board_state[i].append(0)

    # Return the board state
    return board_state


def render(board_state):
    
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


def next_board_state():
    pass


def main():

    height = 22
    width = 10
    board_state = random_state(height, width)
    render(board_state)

main()