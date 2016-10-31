# Tic Tac Toe!!!
# printer83mph's version
import time

def raw_ask(question):
    return raw_input(str(question) + "\n>>> ")

def main():
    print "Welcome to my Tic Tac Toe Game!"
    print "Here's how it works:"
    print "Player X goes first, and then player O"
    print "The grid looks like this:\n"
    print " - | - | - "
    print " - | - | - "
    print " - | - | - \n"

    grid = [[0,0,0],[0,0,0],[0,0,1]]
    turn(1,grid)
    print(grid[2][2])

def turn(ply,grid):
    row = raw_ask("Player " + str(ply) + " Row?")
    column = raw_ask("X Column?")
    if(grid[row-1][column-1] == 0):
        return [row,column]
    else:
        return False

main()