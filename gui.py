# This file will hold the code for the gui which I plan to make using tKinter

import tkinter as tk



# Data for testing
list_title = "Temp for Testing"
todo_list = [("Finish homework due today", 5), ('Go to class', 5), ('Research Job Openings', 4), ('Go to gym', 3),
             ('Take out trash', 2), ('Organize garage', 1)]
task_name = todo_list[0][0]
priority = todo_list[0][1]

window = tk.Tk()

# main window dimensions
WIDTH = 900
HEIGHT = 600
X_POS = 10
Y_POS = 20

# button dimensions
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 2

# initialize main window
window.title("ToDo List App")
window.geometry(f'{WIDTH}x{HEIGHT}+{X_POS}+{Y_POS}')


# create new to-do button
new_todo_button = tk.Button(window, text="New ToDo", background='green', foreground='white', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
new_todo_button.place(x=30, y=30)

# create label for list title
list_title = tk.Label(text=f'{list_title}', foreground='black', width=30, height=2)
list_title.place(x=300, y=100)

# create edit button
edit_button = tk.Button(window, text="Edit", background='yellow', foreground='black', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# create remove button
remove_button = tk.Button(window, text='Remove', background='red', foreground='black', width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

#temp placement for testing
edit_button.place(x=300, y=30)
remove_button.place(x=500, y=30)

# create labels for rows of to-do items
task_label = tk.Label(text='Task', foreground='black', width=30, height=2)
priority_label = tk.Label(text='Priority', foreground='black', width=30, height=2)
done_delete_label = tk.Label(text='Done/Delete', foreground='black', width=30, height=2)

# place labels for rows of to-do items
task_label.place(x=50, y=150)
priority_label.place(x=400, y=150)
done_delete_label.place(x=600, y=150)


# run tkinter main event loop
window.mainloop()

