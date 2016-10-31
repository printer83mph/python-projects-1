import math
import random
#I did all seven projects, here they are!
choice = raw_input ("Projects:\n1.  F-C Calculator\n2.  Distance Between Two Points on a Cartesian Graph\n3.  Heron's Formula\n4.  Armstrong Numbers\n5.  Four Digits\n6.  Perfect Numbers Under 100,000\n7.  Random Guessing Game\n>>> ")


if choice == "1":
    go = "y"
    while not go == "n":
        conversion=raw_input("1: Fahrenheit to Celsius\n2: Celsius to Fahrenheit\n> ")
        if conversion == "1":
            v=input("Temperature in Fahrenheit:\n> ")
            v = (v-32)/1.8
            print v

        if conversion == "2":
            v=input("Temperature in Celsius:\n> ")
            v = (v*1.8)+32
            print v

        go=raw_input("Restart? (y/n)\n> ")


if choice == "2":
    x1 = raw_input("What is the x coordinate of the first point?\n")
    x2 = raw_input("What is the y coordinate of the first point?\n")
    y1 = raw_input("What is the x coordinate of the second point?\n")
    y2 = raw_input("What is the y coordinate of the second point?\n")
    d = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    print d

if choice == "3":
    a = input ("side 1?:\n>>> ")
    b = input ("side 2?:\n>>> ")
    c = input ("side 3?:\n>>> ")
    s = (a + b + c)/2
    A = 1/4*(math.sqrt(s(s - a)(s - b)(s - c)))
    print "Your answer is..."
    print A


if choice == "4":
    for a in range (100,999):
        a = str(a)
        b = ((int(a[0]))**3) + ((int(a[1]))**3) + ((int(a[2]))**3)
        if int(a) == b:
            print a

if choice == "5":
    print "Take a 4 digit number.  Add the first 2 d igits to to the last 2 digits.  Square the sum.  Surprise!  You have the original number again."
    for a in range (1000,9999):
        a = str(a)
        b = ( ((int(a[0]))*10) + (int(a[1])) )
        c = ( ((int(a[2]))*10) + (int(a[3])) )
        d = (b+c)**2
        if d == int(a):
            print ds

if choice == "6":
    a = True
    n = 0
    print "All perfect numbers up to 100,000 are:"
    while a == True:                           #  To loop the following commands
        running = True
        while running == True:
            r = 0
            n =  n+ 1
            for x in range(1,n + 1):
                if n%x == 0:                   #  To determine the factors of n
                    r = r + x
                    if x == n:
                        if  r == 2*n:
                            print n
                            running = False
                        else:
                            running = False

if choice == "7":
    a = random.randint(0,10)
    n = 0
    while 1:
        b = input("Guess the number:\n")
        if b == a:
            n = n + 1
            print "Nice Job!"
            print "You got it in"
            print n
            print "Guesses."
            break
        else:
            n = n + 1
            print "Wrong!"
            print "You have guessed"
            print n
            print "times."
