#Tic Tac Toe!!!
#Maybe a little more complicated than it needs to be...

print "Welcome to my Tic Tac Toe Game!"
print "Here's how it works:"
print "Player X goes first, and then player O"
print "The grid looks like this:\n"
print " t1 | t2 | t3 "
print " m1 | m2 | m3 "
print " b1 | b2 | b3 \n"

go = raw_input("Ready? (y/n)\n>>> ")
while go == "y":
    t1 = " - "
    t2 = " - "
    t3 = " - "
    m1 = " - "
    m2 = " - "
    m3 = " - "
    b1 = " - "
    b2 = " - "
    b3 = " - "
    
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
    
    x1 = raw_input("Player X Position:\n>>> ")
                                                #First Turn (X)
    if x1 == "t1":
        t1 = " X "
    if x1 == "t2":
        t2 = " X "
    if x1 == "t3":
        t3 = " X "
    if x1 == "m1":
        m1 = " X "
    if x1 == "m2":
        m2 = " X "
    if x1 == "m3":
        m3 = " X "
    if x1 == "b1":
        b1 = " X "
    if x1 == "b2":
        b2 = " X "
    if x1 == "b3":
        b3 = " X "
        
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
    
    o1 = raw_input("Player O Position:\n>>> ")
                                                #Second Turn (O)
    if o1 == "t1":
        if o1 != x1:
            t1 = " O "
        else:
            print "Space Occupied"
    if o1 == "t2":
        if o1 != x1:
            t2 = " O "
        else:
            print "Space Occupied"
    if o1 == "t3":
        if o1 != x1:
            t3 = " O "
        else:
            print "Space Occupied"
    if o1 == "m1":
        if o1 != x1:
            m1 = " O "
        else:
            print "Space Occupied"
    if o1 == "m2":
        if o1 != x1:
            m2 = " O "
        else:
            print "Space Occupied"
    if o1 == "m3":
        if o1 != x1:
            m3 = " O "
        else:
            print "Space Occupied"
    if o1 == "b1":
        if o1 != x1:
            b1 = " O "
        else:
            print "Space Occupied"
    if o1 == "b2":
        if o1 != x1:
            b2 = " O "
        else:
            print "Space Occupied"
    if o1 == "b3":
        if o1 != x1:
            b3 = " O "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
    
    x2 = raw_input("Player X Position:\n>>> ")
                                                #Third Turn (X)
    if x2 == "t1":
        if x2 != x1 and x2 != o1:
            t1 = " X "
        else:
            print "Space Occupied"
    if x2 == "t2":
        if x2 != x1 and x2 != o1:
            t2 = " X "
        else:
            print "Space Occupied"
    if x2 == "t3":
        if x2 != x1 and x2 != o1:
            t3 = " X "
        else:
            print "Space Occupied"
    if x2 == "m1":
        if x2 != x1 and x2 != o1:
            m1 = " X "
        else:
            print "Space Occupied"
    if x2 == "m2":
        if x2 != x1 and x2 != o1:
            m2 = " X "
        else:
            print "Space Occupied"
    if x2 == "m3":
        if x2 != x1 and x2 != o1:
            m3 = " X "
        else:
            print "Space Occupied"
    if x2 == "b1":
        if x2 != x1 and x2 != o1:
            b1 = " X "
        else:
            print "Space Occupied"
    if x2 == "b2":
        if x2 != x1 and x2 != o1:
            b2 = " X "
        else:
            print "Space Occupied"
    if x2 == "b3":
        if x2 != x1 and x2 != o1:
            b3 = " X "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3

    o2 = raw_input("Player O Position:\n>>> ")
                                                #Fourth Turn (O)
    if o2 == "t1":
        if o2 != x1 and o2 != o1 and o2 != x2:
            t1 = " O "
        else:
            print "Space Occupied"
    if o2 == "t2":
        if o2 != x1 and o2 != o1 and o2 != x2:
            t2 = " O "
        else:
            print "Space Occupied"
    if o2 == "t3":
        if o2 != x1 and o2 != o1 and o2 != x2:
            t3 = " O "
        else:
            print "Space Occupied"
    if o2 == "m1":
        if o2 != x1 and o2 != o1 and o2 != x2:
            m1 = " O "
        else:
            print "Space Occupied"
    if o2 == "m2":
        if o2 != x1 and o2 != o1 and o2 != x2:
            m2 = " O "
        else:
            print "Space Occupied"
    if o2 == "m3":
        if o2 != x1 and o2 != o1 and o2 != x2:
            m3 = " O "
        else:
            print "Space Occupied"
    if o2 == "b1":
        if o2 != x1 and o2 != o1 and o2 != x2:
            b1 = " O "
        else:
            print "Space Occupied"
    if o2 == "b2":
        if o2 != x1 and o2 != o1 and o2 != x2:
            b2 = " O "
        else:
            print "Space Occupied"
    if o2 == "b3":
        if o2 != x1 and o2 != o1 and o2 != x2:
            b3 = " O "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
        
    x3 = raw_input("Player X Position:\n>>> ")
                                                #Fifth Turn (X)
    if x3 == "t1":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            t1 = " X "
        else:
            print "Space Occupied"
    if x3 == "t2":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            t2 = " X "
        else:
            print "Space Occupied"
    if x3 == "t3":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            t3 = " X "
        else:
            print "Space Occupied"
    if x3 == "m1":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            m1 = " X "
        else:
            print "Space Occupied"
    if x3 == "m2":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            m2 = " X "
        else:
            print "Space Occupied"
    if x3 == "m3":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            m3 = " X "
        else:
            print "Space Occupied"
    if x3 == "b1":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            b1 = " X "
        else:
            print "Space Occupied"
    if x3 == "b2":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            b2 = " X "
        else:
            print "Space Occupied"
    if x3 == "b3":
        if x3 != x1 and x3 != o1 and x3 != x2 and x3 != o2:
            b3 = " X "
        else:
            print "Space Occupied"
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
                                                #If X Wins
    if t1 == " X " and t2 == " X " and t3 == " X ":
        end = raw_input("Player X Wins!\n")
    if m1 == " X " and m2 == " X " and m3 == " X ":
        end = raw_input("Player X Wins!\n")
    if b1 == " X " and b2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m1 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
    if t2 == " X " and m2 == " X " and b2 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m3 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m2 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
        
    o3 = raw_input("Player O Position:\n>>> ")
                                                #Sixth Turn (O)
    if o3 == "t1":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            t1 = " O "
        else:
            print "Space Occupied"
    if o3 == "t2":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            t2 = " O "
        else:
            print "Space Occupied"
    if o3 == "t3":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            t3 = " O "
        else:
            print "Space Occupied"
    if o3 == "m1":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            m1 = " O "
        else:
            print "Space Occupied"
    if o3 == "m2":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            m2 = " O "
        else:
            print "Space Occupied"
    if o3 == "m3":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            m3 = " O "
        else:
            print "Space Occupied"
    if o3 == "b1":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            b1 = " O "
        else:
            print "Space Occupied"
    if o3 == "b2":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            b2 = " O "
        else:
            print "Space Occupied"
    if o3 == "b3":
        if o3 != x1 and o3 != o1 and o3 != x2 and o3 != o2 and o3 != x3:
            b3 = " O "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
                                                #If O Wins
    if t1 == " O " and t2 == " O " and t3 == " O ":
        end = raw_input("Player 0 Wins!\n")
    if m1 == " O " and m2 == " O " and m3 == " O ":
        end = raw_input("Player O Wins!\n")
    if b1 == " O " and b2 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t1 == " O " and m1 == " O " and b1 == " O ":
        end = raw_input("Player O Wins!\n")
    if t2 == " O " and m2 == " O " and b2 == " O ":
        end = raw_input("Player O Wins!\n")
    if t3 == " O " and m3 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t1 == " O " and m2 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t3 == " O " and m2 == " O " and b1 == " O ":
        end = raw_input("Player O Wins!\n")

    x4 = raw_input("Player X Position:\n>>> ")
                                                #Seventh Turn (X)
    if x4 == "t1":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            t1 = " X "
        else:
            print "Space Occupied"
    if x4 == "t2":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            t2 = " X "
        else:
            print "Space Occupied"
    if x4 == "t3":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            t3 = " X "
        else:
            print "Space Occupied"
    if x4 == "m1":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            m1 = " X "
        else:
            print "Space Occupied"
    if x4 == "m2":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            m2 = " X "
        else:
            print "Space Occupied"
    if x4 == "m3":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            m3 = " X "
        else:
            print "Space Occupied"
    if x4 == "b1":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            b1 = " X "
        else:
            print "Space Occupied"
    if x4 == "b2":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            b2 = " X "
        else:
            print "Space Occupied"
    if x4 == "b3":
        if x4 != x1 and x4 != o1 and x4 != x2 and x4 != o2 and x4 != x3 and x4 != o3:
            b3 = " X "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
                                                #If X Wins
    if t1 == " X " and t2 == " X " and t3 == " X ":
        end = raw_input("Player X Wins!\n")
    if m1 == " X " and m2 == " X " and m3 == " X ":
        end = raw_input("Player X Wins!\n")
    if b1 == " X " and b2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m1 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
    if t2 == " X " and m2 == " X " and b2 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m3 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m2 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
        
    o4 = raw_input("Player O Position:\n>>> ")
                                                #Eighth Turn (O)
    if o4 == "t1":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            t1 = " O "
        else:
            print "Space Occupied"
    if o4 == "t2":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            t2 = " O "
        else:
            print "Space Occupied"
    if o4 == "t3":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            t3 = " O "
        else:
            print "Space Occupied"
    if o4 == "m1":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            m1 = " O "
        else:
            print "Space Occupied"
    if o4 == "m2":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            m2 = " O "
        else:
            print "Space Occupied"
    if o4 == "m3":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            m3 = " O "
        else:
            print "Space Occupied"
    if o4 == "b1":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            b1 = " O "
        else:
            print "Space Occupied"
    if o4 == "b2":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            b2 = " O "
        else:
            print "Space Occupied"
    if o4 == "b3":
        if o4 != x1 and o4 != o1 and o4 != x2 and o4 != o2 and o4 != x3 and o4 != o3 and o4 != x4:
            b3 = " O "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
                                                #If O Wins
    if t1 == " O " and t2 == " O " and t3 == " O ":
        end = raw_input("Player 0 Wins!\n")
    if m1 == " O " and m2 == " O " and m3 == " O ":
        end = raw_input("Player O Wins!\n")
    if b1 == " O " and b2 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t1 == " O " and m1 == " O " and b1 == " O ":
        end = raw_input("Player O Wins!\n")
    if t2 == " O " and m2 == " O " and b2 == " O ":
        end = raw_input("Player O Wins!\n")
    if t3 == " O " and m3 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t1 == " O " and m2 == " O " and b3 == " O ":
        end = raw_input("Player O Wins!\n")
    if t3 == " O " and m2 == " O " and b1 == " O ":
        end = raw_input("Player O Wins!\n")
                                
    x5 = raw_input("Player X Position:\n>>> ")
                                                #Ninth Turn (X)
    if x5 == "t1":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            t1 = " X "
        else:
            print "Space Occupied"
    if x5 == "t2":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            t2 = " X "
        else:
            print "Space Occupied"
    if x5 == "t3":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            t3 = " X "
        else:
            print "Space Occupied"
    if x5 == "m1":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            m1 = " X "
        else:
            print "Space Occupied"
    if x5 == "m2":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            m2 = " X "
        else:
            print "Space Occupied"
    if x5 == "m3":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            m3 = " X "
        else:
            print "Space Occupied"
    if x5 == "b1":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            b1 = " X "
        else:
            print "Space Occupied"
    if x5 == "b2":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            b2 = " X "
        else:
            print "Space Occupied"
    if x5 == "b3":
        if x5 != x1 and x5 != o1 and x5 != x2 and x5 != o2 and x5 != x3 and x5 != o3 and x5 != x4 and x5 != o4:
            b3 = " X "
        else:
            print "Space Occupied"
            
    print t1 , t2 , t3
    print m1 , m2 , m3
    print b1 , b2 , b3
                                                #If X Wins
    if t1 == " X " and t2 == " X " and t3 == " X ":
        end = raw_input("Player X Wins!\n")
    if m1 == " X " and m2 == " X " and m3 == " X ":
        end = raw_input("Player X Wins!\n")
    if b1 == " X " and b2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m1 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
    if t2 == " X " and m2 == " X " and b2 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m3 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t1 == " X " and m2 == " X " and b3 == " X ":
        end = raw_input("Player X Wins!\n")
    if t3 == " X " and m2 == " X " and b1 == " X ":
        end = raw_input("Player X Wins!\n")
                                                #Tie End
    print "Tie!"
    go = raw_input("Play Again? (y/n)\n>>> ")
    

        


