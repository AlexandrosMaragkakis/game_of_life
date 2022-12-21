import random

def random_state(height, width):
    
    board = dead_state(height,width)
    board = [[round(random.random()) for _ in range(height)] for _ in range(width)]
    return board

def dead_state(height, width):
    board = list()
    for i in range(height):
        board.append([])
        for j in range(width):
            board[i].append(0) 
    return board

def main():
    height = 3
    width = 4
    board = random_state(height, width)
    print(board)

main()