import tkinter as Tk
from tkinter import*

root = Tk()
root.title("First GUI")
myText = Label(text="My name is",fg="blue",font=20).gridk(row=0,column=0)
myText = Label(text="Natchapol",fg="green",font=20).gridk(row=1,column=1)
myText = Label(text="Aunjai",fg="red",font=20).gridk(row=3,column=2)
root.geometry("300x300")
root.mainloop()