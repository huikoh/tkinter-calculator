from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

var = StringVar()
c = Checkbutton(root, text="Choose your main course", variable=var,onvalue="Pizza",offvalue="Burger")
c.deselect()
c.pack()

def show():
    myLabel = Label(root, text=var.get()).pack()
    

myButton  = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
