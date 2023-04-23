# This file will hold the code for the gui which I plan to make using tKinter

import tkinter as tk
from functools import partial

from ToDoPohlman import ToDoList as tdl, Task

class App:
    def __init__(self):
        self.window = tk.Tk()

        # main window dimensions
        self.WIDTH = 900
        self.HEIGHT = 600
        self.X_POS = 10
        self.Y_POS = 20

        # button dimensions
        self.BUTTON_WIDTH = 20
        self.BUTTON_HEIGHT = 1
        self.window.title("ToDo List App")
        self.window.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')

        # create new to-do button
        new_todo_button = tk.Button(self.window, text="New ToDo", background='green', foreground='white', width=self.BUTTON_WIDTH,
                                    height=self.BUTTON_HEIGHT)
        new_todo_button.place(x=30, y=30)

        # create label for list title
        list_title = tk.Label(text=f'{list1.name}', foreground='black', width=30, height=2)
        list_title.place(x=300, y=100)

        # create edit button
        edit_button = tk.Button(self.window, text="Edit", background='yellow', foreground='black', width=self.BUTTON_WIDTH,
                                height=self.BUTTON_HEIGHT)

        # create remove button
        remove_button = tk.Button(self.window, text='Remove', background='red', foreground='black', width=self.BUTTON_WIDTH,
                                  height=self.BUTTON_HEIGHT)

        # create labels for rows of to-do items
        task_label = tk.Label(text='Task', foreground='black', width=30, height=2)
        priority_label = tk.Label(text='Priority', foreground='black', width=30, height=2)
        done_delete_label = tk.Label(text='Done/Delete', foreground='black', width=30, height=2)

        # place labels for rows of to-do items
        task_label.place(x=50, y=150)
        priority_label.place(x=400, y=150)
        done_delete_label.place(x=600, y=150)

        # loop through all tasks and display on screen
        count = 0
        for todo_item in list1.tasks:
            task_name_label = tk.Label(text=f'{todo_item.title}', foreground='white', background='grey', width=30,
                                       height=1)
            task_priority_label = tk.Label(text=f'{todo_item.priority}', foreground='white', background='grey',
                                           width=30, height=1)
            remove_button = tk.Button(self.window, text='Remove', background='red', foreground='black', width=self.BUTTON_WIDTH,
                                      height=self.BUTTON_HEIGHT, command=partial(self.remove_item, list1, todo_item))

            y_pos = 200 + (30 * count)
            task_name_label.place(x=50, y=y_pos)
            task_priority_label.place(x=400, y=y_pos)
            remove_button.place(x=630, y=y_pos)
            count += 1
        # run tkinter main event loop
        self.window.mainloop()

    def remove_item(self, tdl, todo_item):
        tdl.remove_task(todo_item)
        self.refresh()

    def refresh(self):
        self.window.destroy()
        self.__init__()














# initialize main window
if __name__ == '__main__':
    # Data for testing
    t1 = Task("Finish Final Project", 5)
    t2 = Task("finish fundamental informatics", 2)

    tasks = [t1, t2]

    list1 = tdl("Main", tasks)
    App()




