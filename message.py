from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code here')
root.iconbitmap("1384023.png")

# Other show: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup","Hello World")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You click yes").pack()
    else:
        Label(root, text="You click no").pack()

Button(root, text="popup",command=popup).pack()
mainloop()