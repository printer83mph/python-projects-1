# Tic Tac Toe!!!
# printer83mph's version
import time

def ask(question):
    return input(str(question) + "\n>>> ")

def main():
    print "Welcome to my Tic Tac Toe Game!"
    print "Here's how it works:"
    print "Player X goes first, and then player O"
    print "The grid looks like this:\n"
    print " --- "
    print " --- "
    print " --- \n"

    grid = [[0,0,0],[0,0,0],[0,0,0]]
    ply1_turn = turn(1,grid)
    if(ply1_turn != False):
        grid[ply1_turn[0]][ply1_turn[1]] = 1

    print(grid[2][2])

def turn(ply,grid):
    row = ask("Player " + str(ply) + " Row?")
    column = ask("Player " + str(ply) + " Column?")
    if(grid[row-1][column-1] == 0):
        return [row-1,column-1]
    else:
        return False

main()