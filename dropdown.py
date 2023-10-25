from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

clicked = StringVar()
options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday",
    "Saturday"
]
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options).pack()

def show():
    myLabel = Label(root, text=clicked.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
