#Battleship - Created by Dema Abu Adas, April 25th
#!/usr/bin/python
from random import randint
from guizero import App, warn, info, Waffle, MenuBar, Box, Text, TextBox, PushButton, ButtonGroup

#Generate a point on the matrix
def new():
    global ship_row
    ship_row = randint(0,4)
    global ship_col
    ship_col = randint(0,4)
    print("NEW:",ship_row,ship_col)

    return ship_row, ship_col
#Function to reset matrix and generate new point
def reset():
    ship_row, ship_col = new()
    my_waffle.set_all("white")
    return ship_row, ship_col
#Function to check if we are clicking on the point generated
def check(x,y):

    print("CHECK:", ship_row, ship_col)
    print("x:",x,"y:",y)
    count = 0
    if x == ship_row and y == ship_col:
        my_waffle.set_pixel(y,x, "green")
        info(title="Congradulations!", text="You found the battleship!\n")
    else:
        my_waffle.set_pixel(y,x, "red")
        count += 1
def howto():
    info(title="How to play!", text="This is a very simple game, every matrix has a corresponding button, you need to guess where the random battleship is located!\n Good Luck :-)" )

app = App(title="Battleship!")

#Start the game!
ship_row, ship_col = new()
print("MAIN:",ship_row, ship_col)
#Menu bar
menubar = MenuBar(app, toplevel=["Options"], options=[
[ ["New Game",reset], ["How to Play", howto] ]])
#Matrix to view where you are clicking
p = Text(app, text="Matrix to view:")
my_waffle = Waffle(app, height=5, width=5, pad=1, dim=40, remember=True)

#Maybe keep maybe delete!
#new_game = PushButton(app, command=reset, text="New Game", grid=[0,1])

#Counter:
count = 5;
c = Text(app, text="Matrix to click and play:")

#Matrix to click and play
box2 = Box(app, layout="grid", grid=[0,5])
b1 =  PushButton(box2, command=check, args=[0,0], text=" 1 ", grid=[0,0])
b2 =  PushButton(box2, command=check, args=[0,1], text=" 2 ", grid=[0,1])
b3 =  PushButton(box2, command=check, args=[0,2], text=" 3 ", grid=[0,2])
b4 =  PushButton(box2, command=check, args=[0,3], text=" 4 ", grid=[0,3])
b5 =  PushButton(box2, command=check, args=[0,4], text=" 5 ", grid=[0,4])
b6 =  PushButton(box2, command=check, args=[1,0], text=" 6 ", grid=[1,0])
b7 =  PushButton(box2, command=check, args=[1,1], text=" 7 ", grid=[1,1])
b8 =  PushButton(box2, command=check, args=[1,2], text=" 8 ", grid=[1,2])
b9 =  PushButton(box2, command=check, args=[1,3], text=" 9 ", grid=[1,3])
b10 = PushButton(box2, command=check, args=[1,4], text="10", grid=[1,4])
b11 = PushButton(box2, command=check, args=[2,0], text="11", grid=[2,0])
b12 = PushButton(box2, command=check, args=[2,1], text="12", grid=[2,1])
b13 = PushButton(box2, command=check, args=[2,2], text="13", grid=[2,2])
b14 = PushButton(box2, command=check, args=[2,3], text="14", grid=[2,3])
b15 = PushButton(box2, command=check, args=[2,4], text="15", grid=[2,4])
b16 = PushButton(box2, command=check, args=[3,0], text="16", grid=[3,0])
b17 = PushButton(box2, command=check, args=[3,1], text="17", grid=[3,1])
b18 = PushButton(box2, command=check, args=[3,2], text="18", grid=[3,2])
b19 = PushButton(box2, command=check, args=[3,3], text="19", grid=[3,3])
b20 = PushButton(box2, command=check, args=[3,4], text="20", grid=[3,4])
b21 = PushButton(box2, command=check, args=[4,0], text="21", grid=[4,0])
b22 = PushButton(box2, command=check, args=[4,1], text="22", grid=[4,1])
b23 = PushButton(box2, command=check, args=[4,2], text="23", grid=[4,2])
b24 = PushButton(box2, command=check, args=[4,3], text="24", grid=[4,3])
b25 = PushButton(box2, command=check, args=[4,4], text="25", grid=[4,4])

#Displays the GUI - No code after this!
app.display()
