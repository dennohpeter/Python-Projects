#!/usr/bin/python3
# Python tkinter application that gets user input and shows the entered text on button click
#
from tkinter import * #importing necessary modules

window = Tk() # creating parent widget

window.title("Welcome to tkinter Basics")  # parent title

window.geometry('350x200')   # dimensions

lbl = Label(window, text="Hello")  # Creating Label

lbl.grid(column=0, row=0) # label positioning

txt = Entry(window,width=10)

txt.grid(column=1, row=0)


def clicked():  # method trigered when button is clicked
    res = "User Text is: " + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked)  #Click me btn with event Listener method

btn.grid(column=2, row=0) # button positioning

window.mainloop() # end of program
