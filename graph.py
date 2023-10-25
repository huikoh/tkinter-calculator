import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x100")

def graph():
    house_prices = np.random.normal(20000, 25000, 5000)
    plt.hist(house_prices, bins=50)
    plt.show()
    
my_button = Button(root, text="Graph it!", command=graph)
my_button.pack()

root.mainloop()