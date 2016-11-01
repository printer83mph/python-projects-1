# Tic Tac Toe!!!
# printer83mph's version
import time

def ask(question):
    return input(str(question) + "\n>>> ")

def turn(ply,grid):
    column = ask("Player " + str(ply) + " Column?")
    row = ask("Player " + str(ply) + " Row?")
    if(grid[row-1][column-1] == 0):
        return [row-1,column-1]
    else:
        return False

def ply_won(grid):
    # Check for horizontal victory
    for row in range(0,3):
        if grid[row][0] == grid[row][1] == grid[row][2]:
            return grid[row][0]
    # Check for vertical victory
    for column in range(0,3):
        if(grid[0][column] == grid[1][column] == grid[2][column]):
            return grid[0][column]
    # Check for tl-br victory
    if(grid[0][0] == grid[1][1] == grid[2][2]):
        return grid[0][0]
    # Check for tr-bl victory
    if(grid[0][2] == grid[1][1] == grid[2][0]):
        return grid[1][1]
    return False

def print_grid(grid):
    print("")
    for row in range(0,3):
            current_row = ""
            for column in range(0,3):
                current_row += str(grid[row][column])
            print(" " + current_row)
    print("")

def main():
    print "Welcome to my Tic Tac Toe Game!"
    print "Here's how it works:"
    print "Player 1 goes first, and then player 2"
    print "The grid looks like this:\n"
    print " 000 "
    print " 000 "
    print " 000 \n"

    grid = [[0,0,0],[0,0,0],[0,0,0]]

    while True:
        ply1_turn = turn(1,grid)
        if(ply1_turn != False):
            grid[ply1_turn[0]][ply1_turn[1]] = 1
        print_grid(grid)
        if(ply_won(grid) != 0):
            break
        ply2_turn = turn(2,grid)
        if(ply2_turn != False):
            grid[ply2_turn[0]][ply2_turn[1]] = 2
        print_grid(grid)
        if(ply_won(grid) != 0):
            break

    print(str(ply_won(grid)) + " wins")

if __name__ == "__main__":
    main()
