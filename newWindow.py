from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code here')
root.iconbitmap("1384023.png")

def open():
    global my_img
    top = Toplevel()
    top.title('Second window')
    top.iconbitmap("1384023.png")
    my_img = ImageTk.PhotoImage(Image.open("1.png"))
    lbl = Label(top,image=my_img).pack()
    btn2 = Button(top, text="Close window",command=top.destroy).pack()

btn = Button(root, text="open second window", command=open).pack()




mainloop()