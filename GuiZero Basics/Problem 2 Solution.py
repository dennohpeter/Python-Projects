#!/usr/bin/python3
# Python GUI application that includes 5 design widgets
#
from guizero import App, Text, PushButton, Window, Picture, warn, yesno, info, error

# You only need to import each widget once, and then you can
# use it in your program as many times as you like.


def warn_btnMethod():
    warn("Uh oh!", "You are almost out of biscuits!")


def yesnoMethod():
    build_a_snowman = yesno("A question...", "Do you want to build a snowman?")
    if build_a_snowman == True:
        info("Snowman", "It doesn't have to be a snowman")
    else:
        error("Snowman", "Okay bye...")


def buttonMethod():
    info("Button Widget", "I know, you clicked!")


def textMethod():
    Text(parent_widget, text="Welcome to 5 widget PythonGUI App\
    This is a python application that shows usage and demonistration of 5 differnt python Gui design widgets")


def gotoPic():
    picture_widget.show()


def backfromPic(window):
    parent_widget.hide()


parent_widget = App(title="PythonGUI with 5 design widgets")
picture_widget = Window(parent_widget, title="guizero picture widget", width=500, height=270, layout="grid")
picture_widget.hide()
picture1 = Picture(picture_widget, image="Outer_space.png", grid=[0, 0])
picture2 = Picture(picture_widget, image="parallax2.png", grid=[1, 0])
picture3 = Picture(picture_widget, image="setup.png", grid=[2, 0, 1, 2])
picture4 = Picture(picture_widget, image="comp.gif", grid=[0, 1, 2, 1])

picture_btn = PushButton(parent_widget, text="Picture Widget", command=gotoPic)

warn_btn = PushButton(parent_widget, text="Warn Widget", command=warn_btnMethod)
yesno_btn = PushButton(parent_widget, text="yesno Widget", command=yesnoMethod)
button_widget = PushButton(parent_widget, text="Button Widget", command=buttonMethod)
text_widget = PushButton(parent_widget, text="Text Widget", command=textMethod)
parent_widget.display()
