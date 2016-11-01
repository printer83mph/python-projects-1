import random

print "Welcome to the Cows and Bulls Game!\n"
print "In this game, a four digit number is generated.\nYou guess the number untill you guess correctly.\nIf you guess a number in the CORRECT space, you get a cow.\nIf you guess a CORRECT number in an INCORRECT space, you get a bull.\nGetting four cows means that you have guessed the number correctly.\nHave fun!"

num = random.randint(1000,9999)
num = str(num)
print num
while num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[0] or num[1] == num[2] or num[1] == num[3] or num[2] == num[0] or num[2] == num[1] or num[2] == num[3] or num[3] == num[0] or num[3] == num[1] or num[3] == num[2]:
    num = random.randint(1000,9999)
    num = str(num)
    print num
cows = 0
bulls = 0
guesses = 0
while cows != 4:
    cows = 0
    bulls = 0
    guess = input("\nGuess the Number:\n>>> ")
    guess = str(guess)
    num = str(num)
                            #Find # of cows
    if guess[0] == num[0]:
        cows += 1
    if guess[1] == num[1]:
        cows += 1
    if guess[2] == num[2]:
            cows += 1
    if guess[3] == num[3]:
        cows += 1
                            #Find # of bulls
    if guess[0] == num[1] or guess[0] == num[2] or guess[0] == num[3]:
        bulls += 1
    if guess[1] == num[0] or guess[1] == num[2] or guess[1] == num[3]:
        bulls += 1
    if guess[2] == num[1] or guess[2] == num[0] or guess[2] == num[3]:
        bulls += 1
    if guess[3] == num[1] or guess[3] == num[2] or guess[3] == num[0]:
        bulls += 1

                            #Print answers
    guesses += 1
    if cows == 4:
        print "You got it!"
        print guesses
    else:
        print "\nCows:", cows
        print "Bulls:", bulls
