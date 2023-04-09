# This file will hold the code for the gui which I plan to make using tKinter

import tkinter as tk

window = tk.Tk()

# main window dimensions
WIDTH = 900
HEIGHT = 600
X_POS = 10
Y_POS = 20

# button dimensions
BUTTON_WIDTH = 30
BUTTON_HEIGHT = 2

# initialize main window
window.title("ToDo List App")
window.geometry(f'{WIDTH}x{HEIGHT}+{X_POS}+{Y_POS}')


# create new to-do button
new_todo_button = tk.Button(window, text="New ToDo", background='green', foreground='white', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
new_todo_button.place(x=30, y=30)

# create label for list title
list_title = tk.Label(text="My List", foreground='black', width=30, height=2)
list_title.place(x=300, y=100)




# run tkinter main event loop
window.mainloop()

