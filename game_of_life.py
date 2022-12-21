import random

def random_state(height, width):
    
    board_state = dead_state(height,width)

    # default threshold = 0.5
    # TODO make threshold adjustable
    board_state = [[round(random.random()) for _ in range(height)] for _ in range(width)]
    return board_state

def dead_state(height, width):

    board_state = list()
    for i in range(height):
        board_state.append([])
        for j in range(width):
            board_state[i].append(0) 
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

def main():

    height = 20
    width = 10
    board_state = random_state(height, width)
    render(board_state)

main()