# APR
# 10/27/2025
# 005
# CSCE 101 Final Project
# TIC TAC TOE

"""DESCRIPTION:
My Project involves using turtles to print the board and pieces as playersinput on prompt where to place them.
Locations will be traced using arrays being passed through comparison operators to find a winner. Player selectability will be attemptes"""

# imports
import turtle, random, time

# functions
def makeBoard():
    # imports
    import turtle, random, time

    global running, inputs, contChoice
    #variables
    running = True

    #valid user location inputs
    inputs = ["tl", "t", "tr", "l", "c", "r", "bl", "b", "br"]
    contChoice = ["yes","no"]
    
    # screen creation
    global screen
    screen = turtle.Screen()
    screen.bgcolor("tan")
    screen.title("Tic Tac Toe: CSCE101 FP")
    screen.tracer(0)
    
    #makes the double array for board traking
    global empty, board, gmove
    gmove = 0
    
    empty = "z"
    #######double list "how to" provided by GPT
    board = [[empty for row in range(3)] for cell in range(3)]
    #######GPT exchange leading to the above code
    #question: how do i use a python list in the same way as a java double array
    #answer:
    # In Java, a double array (e.g. double[][] arr) is typically a 2D array —
    # a rectangular matrix of numbers with fixed dimensions.
    # In Python, you can represent and use the same concept in several ways, depending on what you need:
    #   if your java code has:
    #       double[][] arr = new double[2][2];
    #       arr[0][2] = 5.5;
    #   then in python you can do:
    #       arr = [[0.0 for _ in range(2)] for _ in range(2)]
    #       arr[0][2] = 5.5
    #######

    #make peices
    global pieces, piece
    pieces = []
    for i in range(12):
        piece = turtle.Turtle()
        piece.hideturtle()
        piece.shapesize(5)
        pieces.append(piece)
        
    #board location variables for comparision use (can't be used for assignment to board location)
    #top
    global TL, T, TR

    TL = board[0][0]#(-130,130)
    T = board[0][1]#(10,130)
    TR = board[0][2]#(150,130)
    #middle
    global L, C, R
    
    L = board[1][0]#(-130,0)
    C = board[1][1]#(10,0)
    R = board[1][2]#(150,0)
    #bottom
    global BL, B, BR

    BL = board[2][0]#(-130,-150)
    B = board[2][1]#(10,-150)
    BR = board[2][2]#(150,-150)

    # turtle creation
    #board drawing creation
    global bD
    bD = turtle.Turtle()
    bD.hideturtle()

    bD.fillcolor("seagreen")
    bD.begin_fill()
    writeCords(bD,-200,200,False,0)
    for i in range(4):
        bD.forward(425)
        bD.right(90)
    bD.end_fill()

    #board dividing lines verticle
    #writeCords(bD,-60,200,False,0)
    bD.pensize(5)
    bD.pencolor("black")
    writeCords(bD,-60,200,False,0)    
    bD.right(90)
    bD.forward(425)

    writeCords(bD,90,200,True,425)
    #bD.forward(425)

    #board dividing lines horizon
    writeCords(bD,-200,70,False,0)
    bD.left(90)
    bD.forward(425)

    writeCords(bD,-200,-70,True,425)
    #bD.forward(425)

    #game name writing
    writeCords(bD,-85,270,False,0)
    bD.pensize(10)
    bD.write("TIC TAC TOE", font=("times", 24, "bold"))

    writeCords(bD,-125,210,False,0)
    bD.write("Valid inputs are: TL, T, TR, L, C, R, BL, B, BR", font=("times",12,"normal"))

    screen.update()
    
#####helper function
def writeCords(turtle,x,y,forward,fdist):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    if (forward == True):
        turtle.forward(fdist)
        
#####dialogue functions
def gamecont():
    global screen, running, pieces, board, bD
    againQ = True
    again = screen.textinput("Continue Choice","Would you like to play again? Yes or No.")
    while(againQ):
        again = again.strip().lower()
        if (again not in contChoice):
            again = screen.textinput("Continue Choice","Would you like to play again? Yes or No.")
        else: 
            againQ = False

    if (again == "yes"):
        screen.clearscreen()
        running = True
        pieces.clear()
        board.clear()
        gameplay()   
    if (again == "no"):
        bD.undo()
        writeCords(bD,-300,200,False,0)
        bD.write("Thanks for playing, bye.",font=("times",50,"normal"))
        screen.update()
        time.sleep(3)
        turtle.bye()
        #####GPT provided code to prevent confirm kill popup
        import sys
        sys.exit()
        #####
        
def playerMove():
    global gmove
    if gmove%2 == 0:
        player = 1
    elif gmove%2 == 1:
        player = 2 
    #player move request
    setM = True
    move = screen.textinput(f"Player {player} move","Enter location")
    #removes white space and forces it to lower case
    move = move.strip().lower()

    #takes move until valid
    while(setM):
        if ((move is None)or(move not in inputs)):
            move = screen.textinput(f"Player {player} move","Enter location")
            move = move.strip().lower()
        else: 
            setM = False
    #moves player
    xoPlayer(move)
    
#####win conditions  
def xWin():
    global running
    playvar = "x"
    #horizontal win
    if (((board[0][0].lower() == playvar)and(board[0][1].lower() == playvar)and(board[0][2].lower() == playvar))or
        ((board[1][0].lower() == playvar)and(board[1][1].lower() == playvar)and(board[1][2].lower() == playvar))or
        ((board[2][0].lower() == playvar)and(board[2][1].lower() == playvar)and(board[2][2].lower() == playvar))):
        running = False
        return True
    #vertical win
    elif (((board[0][0].lower() == playvar)and(board[1][0].lower() == playvar)and(board[2][0].lower() == playvar))or
          ((board[0][1].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][1].lower() == playvar))or
          ((board[0][2].lower() == playvar)and(board[1][2].lower() == playvar)and(board[2][2].lower() == playvar))):
        running = False
        return True
    #diaganol win
    elif (((board[0][0].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][2].lower() == playvar))or
          ((board[0][2].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][0].lower() == playvar))):
        running = False
        return True
    else:
        return False

def oWin():
    global running
    playvar = "o"
    #horizontal win
    if (((board[0][0].lower() == playvar)and(board[0][1].lower() == playvar)and(board[0][2].lower() == playvar))or
        ((board[1][0].lower() == playvar)and(board[1][1].lower() == playvar)and(board[1][2].lower() == playvar))or
        ((board[2][0].lower() == playvar)and(board[2][1].lower() == playvar)and(board[2][2].lower() == playvar))):
        running = False
        return True
    #vertical win
    elif (((board[0][0].lower() == playvar)and(board[1][0].lower() == playvar)and(board[2][0].lower() == playvar))or
          ((board[0][1].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][1].lower() == playvar))or
          ((board[0][2].lower() == playvar)and(board[1][2].lower() == playvar)and(board[2][2].lower() == playvar))):
        running = False
        return True
    #diaganol win
    elif (((board[0][0].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][2].lower() == playvar))or
          ((board[0][2].lower() == playvar)and(board[1][1].lower() == playvar)and(board[2][0].lower() == playvar))):
        running = False
        return True
    else:
        return False
    
def draw():
    global running, board, empty
    if (xWin() != True) and (oWin() != True):
        if ((board[0][0] != empty)and(board[0][1] != empty)and(board[0][2] != empty)and
            (board[1][0] != empty)and(board[1][1] != empty)and(board[1][2] != empty)and
            (board[2][0] != empty)and(board[2][1] != empty)and(board[2][2] != empty)):
            running = False
            return True
        else:
            return False
    else:
        return False

def gameDone():
    if ((xWin() == True) or (oWin()==True)or(draw() == True)):
        return True
    else:
        return False

#####move validation functions
def compMove():
    global gmove, empty
    
    #available spaces       
    if (not gameDone()):
        xCord = random.randint(0,2)
        yCord = random.randint(0,2)
        #empty found
        if (board[xCord][yCord] == empty):
            if gmove %2 == 0:
                board[xCord][yCord] = "x"
                pieces[gmove].shape("triangle")
            if gmove % 2 == 1:
                board[xCord][yCord] = "o"
                pieces[gmove].shape("circle")
            time.sleep(.5)

            #row 1
            if (xCord == 0 and yCord == 0):#00
                pieces[gmove].setposition(-130,130)
            if (xCord == 0 and yCord == 1):#01
                pieces[gmove].setposition(10,130)
            if (xCord == 0 and yCord == 2):#02
                pieces[gmove].setposition(150,130)
            #row 2
            if (xCord == 1 and yCord == 0):#10
                pieces[gmove].setposition(-130,0)
            if (xCord == 1 and yCord == 1):#11
                pieces[gmove].setposition(10,0)
            if (xCord == 1 and yCord == 2):#12
                pieces[gmove].setposition(150,0)
            #row 3
            if (xCord == 2 and yCord == 0):#20
                pieces[gmove].setposition(-130,-150)
            if (xCord == 2 and yCord == 1):#21
                pieces[gmove].setposition(10,-150)
            if (xCord == 2 and yCord == 2):#22
                pieces[gmove].setposition(150,-150)
            pieces[gmove].showturtle()
            screen.update()
            gameDone()
            gmove += 1
            
        #not yet empty found
        else:
            compMove()

def xoPlayer(move):
    global gmove
    
    if not gameDone():#checks if win conditions are met befor assignment
        time.sleep(.2)
        setPiece(move)
        #depending on the move sets traker to x or o
        if gmove %2 == 0:
            pChar = "x"
        if gmove % 2 == 1:
            pChar = "o"
        time.sleep(.5)
        if (move == "tl"):
            board[0][0] = pChar
        if (move == "t"):
            board[0][1] = pChar
        if (move == "tr"):
            board[0][2] = pChar
        if (move == "l"):
            board[1][0] = pChar
        if (move == "c"):
            board[1][1] = pChar
        if (move == "r"):
            board[1][2] = pChar
        if (move == "bl"):
            board[2][0] = pChar
        if (move == "b"):
            board[2][1] = pChar
        if (move == "br"):
            board[2][2] = pChar
        gameDone() #checks for win after move   
        gmove += 1  

#####gui update
def setPiece(move):
    global gmove, pieces, screen
    
    if not gameDone():
        if gmove %2 == 0:
            pieces[gmove].shape("triangle")
        if gmove % 2 == 1:
            pieces[gmove].shape("circle")
        #row 1
        if (move == "tl"):
            pieces[gmove].setposition(-130,130)
        if (move == "t"):
            pieces[gmove].setposition(10,130)
        if (move == "tr"):
            pieces[gmove].setposition(150,130)
        #row 2
        if (move == "l"):
            pieces[gmove].setposition(-130,0)
        if (move == "c"):
            pieces[gmove].setposition(10,0)
        if (move == "r"):
            pieces[gmove].setposition(150,0)
        #row 3
        if (move == "bl"):
            pieces[gmove].setposition(-130,-150)
        if (move == "b"):
            pieces[gmove].setposition(10,-150)
        if (move == "br"):
            pieces[gmove].setposition(150,-150)
        pieces[gmove].showturtle()
    screen.update()
    
#####game run functions 
def gameplay():
    global running, gmove
    makeBoard()
    while(running):        
        if(gameDone()):
            running = False
        else:            
            #get number of players
            setPC = True
            playerCount = int(screen.numinput("Player Count","How many players? 0,1,2"))
            while(setPC):
                if ((playerCount is None)or(0>playerCount)or(playerCount>2)):
                    playerCount = int(screen.numinput("Player Count","How many players? 0,1,2"))
                else: 
                    setPC = False

            # single player code
            if (playerCount == 1):     
                    while not gameDone():
                        if not gameDone():
                            playerMove()   
                        if not gameDone():
                            #moves computer
                            compMove()
                            
            # two player code
            if (playerCount == 2):
                while not gameDone():
                    if not gameDone():
                        playerMove()          
                    if not gameDone():
                        playerMove()

                # zero player code
            if (playerCount == 0):
                while not gameDone():
                    compMove()               

    if(draw() == True):
        bD.undo()
        writeCords(bD,-280,220,False,0)
        bD.write("The game has come to a draw. No one wins.", font=("times",24,"normal"))       
        gamecont()               
    if(xWin() == True):
        bD.undo()
        writeCords(bD,-250,200,False,0)
        bD.write("Player One wins!",font=("times",24,"normal"))       
        gamecont()
    if(oWin() == True):
        bD.undo()
        writeCords(bD,-250,200,False,0)
        bD.write("Player Two Wins!",font=("times",24,"normal"))
        gamecont()
              
#game start
gameplay()
