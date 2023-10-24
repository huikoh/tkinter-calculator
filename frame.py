from tkinter import *

root = Tk()
root.title('Learn To Code here')
root.iconbitmap("1384023.png")

frame = LabelFrame(root, text="This is my frame",padx=50,pady=50)
frame.pack(padx=100,pady=100)

b = Button(frame, text="Dont click here")
b.grid(row=0,column=0)
b2 = Button(frame, text="Dont click here")
b2.grid(row=1,column=1)

frame = LabelFrame(root, text="Second frame",padx=50,pady=50)
frame.pack(padx=100,pady=100)
b = Button(frame, text="Dont click here")
b.pack()
b2 = Button(frame, text="Dont click here")
b2.pack()

root.mainloop()