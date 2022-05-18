wordLst=["armand ortiz", "baseball", "homeless", "zipper", "gnarly", "janitor", "computer", "batman", "hereditary", "vampire", "mike wazowski", "python", "barack obama", "calculus", "football player", "yoda", "progress report", "lady gaga", "abraham lincoln", "russell wilson", "defenestrate", "airpods", "cheese", "calendar", "hypothesis", "seattle", "juxtaposition", "snack attack", "sicko mode", "axiom", "askew", "swimming pool"]

import turtle
DK=turtle.Turtle()
paucek=turtle.Turtle()
DK.penup()
gameScore=0

t=-400
h=-200

gameOver=False 


import random
gameWord=random.choice(wordLst)#this uses the random module to choose a random word for the game
gameWord=gameWord.upper()
letters=[]
for i in gameWord:
    letters.append(i)#this isolates each letter in the word
if letters.count(" ")==1:
    gameScore=1

DK.penup()
DK.goto(-300, 360)
DK.pendown()
DK.right(90)
DK.forward(35)
DK.right(180)
DK.forward(60)
DK.right(-90)
DK.forward(120)
DK.right(-90)
DK.forward(350)
DK.right(90)
DK.forward(30)
DK.right(180)
DK.forward(60)
DK.penup()



hangman=0

broke=gameWord.split(" ")#splits the word into two if it's two words

spaces=len(gameWord)

distance=850//spaces#decides where the word shuld start in order to make the spacing work

coords=[]

armandOrtiz=-475+distance

def line(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.pendown()
    paucek.forward(45)


for i in range(len(broke[0])):#draws out the spaces for letters
    line(armandOrtiz, -50)
    coords.append(armandOrtiz)
    armandOrtiz+=60
armandOrtiz+=60
try:
    for i in range(len(broke[1])):#creates the spaces for the second word, but uses a tryexcept just in case it's only one word
        line(armandOrtiz, -50)
        coords.append(armandOrtiz)
        armandOrtiz+=60
        
except IndexError:
    pass

   
    #below is all the letters for turtle put as functions so they can be called

def A(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.pendown()
    paucek.left(65)
    paucek.forward(50)
    paucek.right(130)
    paucek.forward(50)
    paucek.forward(-25)
    paucek.right(115)
    paucek.forward(23)
    paucek.right(180)
    

def Y(x, y):
    
    paucek.up()
    paucek.goto(x, y)
    paucek.forward(22)
    paucek.down()
    paucek.right(-90)
    paucek.forward(30)
    paucek.right(45)
    paucek.forward(25)
    paucek.forward(-25)
    paucek.left(90)
    paucek.forward(25)
    paucek.right(135)

def T(x, y):
    
    paucek.penup()
    paucek.goto(x, y)
    
    paucek.fd(23)
    paucek.left(90)
    paucek.down()
    paucek.forward(45)
    paucek.right(90)
    paucek.forward(22)
    paucek.backward(44)
    
def H(x, y):
    
    paucek.penup()
    paucek.goto(x, y)
    paucek.forward(8)
    paucek.pendown()
    paucek.left(90)
    paucek.forward(45)
    paucek.backward(22.5)
    paucek.right(90)
    paucek.forward(30)
    paucek.right(90)
    paucek.forward(22.5)
    paucek.backward(45)
    paucek.left(90)

def O(x, y):

    paucek.penup()
    paucek.goto(x, y)
    paucek.forward(22.5)
    paucek.down()
    paucek.circle(23.5, 360)
    
def N(x, y):
    paucek.penup()
    paucek.goto(x, y)
    
    paucek.left(90)
    paucek.pendown()
    paucek.fd(100//2)
    paucek.right(140)
    paucek.fd(120//2)
    paucek.left(140)
    paucek.fd(100//2)
    paucek.bk(100//2)
    paucek.right(90)

def C(x, y):
    paucek.up()
    paucek.goto(x, y)
    paucek.forward(40)
    paucek.left(90)
    
    paucek.right(90)
    paucek.down()
    paucek.circle(22.5, -180)
    paucek.right(180)
    
def D(x, y):
    
    paucek.penup()
    paucek.goto(x, y)
    paucek.fd(15)
    
    paucek.pendown()
    paucek.circle(22.5,180)
    paucek.left(90)
    paucek.fd(45)
    paucek.right(270)


def B(x, y):
    
    paucek.penup()
    paucek.goto(x, y)
    paucek.pendown()
    paucek.right(-90)
    paucek.forward(45)
    paucek.right(90)
    paucek.circle(-11.25, 180)
    paucek.circle(11.25, -180)
    

def R(x, y):
    paucek.penup()
    paucek.goto(x+20, y)
    paucek.pendown()
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
    paucek.circle(-15, 180)
    paucek.left(135)
    paucek.forward(25.5)
    paucek.left(45)

def P(x, y):
    paucek.penup()
    paucek.goto(x+20, y)
    paucek.pendown()
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
    paucek.circle(-15, 180)
    paucek.left(180)
    
    
def K(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.pendown()
    paucek.left(90)
    paucek.forward(45)
    paucek.backward(22.5)
    paucek.right(45)
    paucek.forward(26.4)
    paucek.backward(26.6)
    paucek.right(90)
    paucek.forward(26.4)
    paucek.left(45)
    
def E(x, y):
    paucek.penup()
    paucek.goto(x, y+1)
    paucek.forward(7)
    paucek.down()
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
    paucek.forward(30)
    paucek.backward(30)
    paucek.right(90)
    paucek.forward(22.5)
    paucek.left(90)
    paucek.forward(30)
    paucek.forward(-30)
    paucek.right(90)
    paucek.forward(22.5)
    paucek.left(90)
    paucek.forward(30)

def F(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.forward(7)
    paucek.down()
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
    paucek.forward(30)
    paucek.backward(30)
    paucek.right(90)
    paucek.forward(22.5)
    paucek.left(90)
    paucek.forward(20)
    paucek.forward(-20)
    paucek.right(90)
    paucek.forward(22.5)
    paucek.left(90)
    
def M(x, y):
    paucek.penup()
    paucek.goto(x ,y)
    paucek.down()
    paucek.left(90)
    paucek.forward(45)
    paucek.right(160)
    paucek.forward(47.89)
    paucek.left(140)
    paucek.forward(47.89)
    paucek.right(160)
    paucek.forward(45)
    paucek.left(90)

def X(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.pendown()
    paucek.left(45)
    paucek.forward(63.6)
    paucek.backward(63.6//2)
    paucek.left(90)
    paucek.forward(63.6//2)
    paucek.backward(63.62)
    paucek.right(135)


def I(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.forward(22.5)
    paucek.left(90)
    paucek.pendown()
    paucek.fd(30)
    paucek.penup()
    paucek.fd(7)
    paucek.pendown()
    paucek.circle(2, 360)
    paucek.right(90)
def Z(x, y):
    paucek.penup()
    paucek.goto(x+5, y+36)
    paucek.pendown()
    paucek.forward(35)
    paucek.right(135)
    paucek.forward(49.4)
    paucek.right(225)
    paucek.forward(35)
def L(x, y):
    paucek.penup()
    paucek.goto(x+5, y+1)
    paucek.pendown()
    paucek.forward(35)
    paucek.forward(-35)
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
def W(x, y):
    paucek.penup()
    paucek.goto(x, y+45)
    paucek.pendown()
    paucek.right(75)
    paucek.forward(43.89)
    paucek.left(150)
    paucek.forward(43.89)
    paucek.right(150)
    paucek.forward(43.89)
    paucek.left(150)
    paucek.forward(43.89)
    paucek.right(75)


def S(x, y):
    paucek.penup()
    paucek.goto(x+22.5, y+45)
    paucek.pendown()
    paucek.circle(-22.5//2, -160)
    paucek.circle(22.5//2,-200)
    paucek.right(320)


def V(x, y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.forward(23)
    paucek.pendown()
    paucek.left(110)
    paucek.forward(47.89)
    paucek.backward(47.89)
    paucek.right(40)
    paucek.forward(47.89)
    paucek.right(70)
    
def G(x, y):
    paucek.penup()
    paucek.goto(x , y)
    paucek.left(90)
    paucek.forward(45)
    paucek.right(90)
    paucek.forward(23)
    paucek.pendown()
    paucek.circle(-23, -180)
    paucek.left(-90)
    paucek.forward(15)
    paucek.left(-90)
    paucek.forward(-5)
   
   
def J(x , y):
    paucek.penup()
    paucek.goto(x, y)
    paucek.right(-90)
    paucek.forward(10)
    paucek.pendown()
    paucek.circle(-10, -180)
    paucek.forward(-35)
    paucek.right(-90)
    paucek.forward(10)
    paucek.backward(20)
    
def Q(x, y):
    paucek.penup()
    paucek.goto(x , y)
    paucek.forward(22)
    paucek.pendown()
    paucek.circle(23.5)
    paucek.penup()
    paucek.forward(10)
    paucek.left(90)
    paucek.forward(16)
    paucek.right(135)
    paucek.pendown()
    paucek.forward(20)
    paucek.left(45)
def U(x, y):
    paucek.penup()
    paucek.goto(x , y)
    paucek.left(90)
    paucek.forward(45)
    paucek.pendown()
    paucek.backward(25)
    paucek.circle(-20, -180)
    paucek.forward(-25)
    paucek.left(90)
    #below is all the functions that draw out the hangingman character
def hangingman1():
    DK.goto(-300, 250)
    DK.pendown()
    DK.circle(40, 360)

def hangingman2():
    
    DK.right(90)
    DK.forward(100)
    DK.left(90)   
   
def hangingman3():
    
    DK.right(45)
    DK.forward(60)
    DK.backward(60)
    DK.left(45)
    
def hangingman4():
    
    DK.right(135)
    DK.forward(60)
    DK.backward(60)
    DK.left(135)
    
def hangingman5():
    
    DK.left(90)
    DK.forward(50)
    DK.right(135)
    DK.forward(40)
    DK.backward(40)
    DK.right(45)
    
def hangingman6():
    
    DK.left(315)
    DK.forward(40)
    DK.right(135)

def hangingman7():
    DK.penup()
    DK.right(45)
    DK.forward(40)
    DK.left(45)
    DK.forward(95)
    DK.right(90)
    DK.forward(-10)
    DK.down()
    DK.begin_fill()
    DK.circle(5,360)
    DK.end_fill()
    DK.up()
    DK.forward(20)
    DK.down()
    DK.begin_fill()
    DK.circle(5, 360)
    DK.end_fill()
    DK.up()
    DK.backward(10)
    DK.right(90)
    DK.forward(25)
    DK.left(90)
    DK.down()
    DK.color("red")
    DK.begin_fill()
    DK.forward(25)

    DK.right(90)
    
    DK.circle(-12.5, 60)#inspired by https://www.geeksforgeeks.org/draw-ellipse-using-turtle-in-python/#:~:text=Draw%20design%20using%20ellipse%20Shape%20The%20following%20steps,Set%20Screen%20Divide%20the%20ellipse%20into%20four%20arcs3
    DK.circle(-30, 60)
    DK.circle(-12.5, 60)
    DK.right(90)
    DK.forward(25)
    DK.end_fill()
    DK.left(90)
    DK.up()
    DK.forward(15)
    DK.begin_fill()
    DK.circle(8, 360)
    DK.end_fill()
def hangingman8():
    DK.penup()
    DK.speed(10)
    DK.forward(57)
    DK.right(180)
    DK.forward(20)
    
    
    DK.pendown()
    DK.begin_fill()
    DK.right(430)
    
    for i in range(5):
        DK.circle(7, 220)
        DK.left(190)
    for i in range(3):
        DK.circle(7, 173)
        DK.left(190)
    for i in range(4):
        DK.circle(7, 220)
        DK.left(190)
    DK.circle(8, 220)
    DK.end_fill()
    DK.speed(5)
def hangingman9():
    DK.penup()
    DK.stamp()
    DK.color("black")
    DK.setheading(270)
    DK.forward(122.5)
    DK.left(45)
    DK.forward(35)
    DK.left(100)
    DK.pendown()
    DK.forward(120)
    DK.color("red")
    DK.right(60)
    DK.begin_fill()
    DK.circle(45, 40)
    for i in range(2):
        
        DK.circle(30, 140)
    DK.circle(25, 40)
    DK.end_fill()
    
    
    
guessedWords=[]
broken=[]
for willy in broke[0]:
    broken.append(willy)
try:
    for lachy in broke[1]:
        broken.append(lachy)
except IndexError:
    pass


coords=list(zip(broken, coords))#I zip these variables together so that the correct letters will go to the correct spots




while gameOver==False:
    guess=input("Guess bro")
    guess=guess.upper()#allow lower and upper case letters to work
    if len(guess)>1:#prevents too many letters from being submitted at once
        print("One letter pls")
        continue
    
    if guessedWords.count(guess)>0:#prevents repeats
        print("already guessed that buddy")
        continue
    guessedWords.append(guess)  

    if letters.count(guess)==0:
        print("L bozo + ratio")
        hangman+=1
        manhang=str(hangman)
        drawing="hangingman" + manhang
        locals()[drawing]()#this whole process makes it so the correct hangman function is called, based on the score
        paucek.color("red")
        locals()[guess](t, h)
     #   guessedWords.append(guess)
        t+=60#moves the next letter over one
    for ache in coords:
        
        if ache[0].count(guess)>0:
            
            paucek.color("green")    
            for pen in ache[0]:
                if pen.count(guess)>0:
                    print("good")
                    gameScore+=pen.count(guess)
                    locals()[pen](ache[1], -50)
                    
        
            
         
            
        
        
    if t==380:
        t=-400
        h=-300

    if gameScore==spaces:
        gameOver=True
        print("You won")
        paucek.speed(10)
        Y(-100, 50)
        O(-40, 50)
        U(20, 50)
        W(120, 50)
        O(180, 50)
        N(240, 50)
        
    if hangman==9:
        gameOver=True
        print("You lost")
        paucek.speed(10)
        G(-100, 50)
        A(-40,50)
        M(20,50)
        E(80,50)
        O(180,50)
        V(240,50)
        E(300,50)
        R(350,50)
    
    
