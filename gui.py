# This file will hold the code for the gui which I plan to make using tKinter

import tkinter as tk

window = tk.Tk()

WIDTH = 900
HEIGHT = 600
X_POS = 10
Y_POS = 20

window.title("ToDo List App")
window.geometry(f'{WIDTH}x{HEIGHT}+{X_POS}+{Y_POS}')
window.mainloop()