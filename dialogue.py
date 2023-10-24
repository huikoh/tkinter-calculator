from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\SCSM11\\Documents\\Code 2023\\tkinterlearning",
        title="Select a file",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    

my_btn = Button(root, text="Open File", command=open).pack()
root.mainloop()
