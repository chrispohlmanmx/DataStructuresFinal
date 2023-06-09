# This file will hold the code for the gui which I plan to make using tKinter

import tkinter as tk
from functools import partial

from ToDoPohlman import ToDoList, Task

class App:
    def __init__(self, tdl=[]):
        self.window = tk.Tk()

        # main window dimensions
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.X_POS = 10
        self.Y_POS = 20

        # button dimensions
        self.BUTTON_WIDTH = 20
        self.BUTTON_HEIGHT = 1

        self.todo_list = ToDoList("Main", tdl)

        self.window.title("ToDo List App")
        self.window.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')


        self.create_render_main_screen()



    def create_render_main_screen(self):

        # create new to-do button
        self.new_todo_button = tk.Button(self.window, text="New ToDo", background='green', foreground='white', width=self.BUTTON_WIDTH,
                                    height=self.BUTTON_HEIGHT, command=self.create_new_todo)
        self.new_todo_button.place(x=30, y=30)

        # create label for list title
        list_title = tk.Label(text=f'{self.todo_list.name or "Master"}', foreground='black', width=30, height=2)
        list_title.place(x=300, y=100)

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
        q = self.todo_list.create_priority_queue()
        while q.isEmpty() == False:
            todo_item = q.pop()
            task_name_label = tk.Label(text=f'{todo_item.title}', foreground='white', background='grey', width=30,
                                       height=1)
            task_priority_label = tk.Label(text=f'{todo_item.priority}', foreground='white', background='grey',
                                           width=30, height=1)
            edit_button = tk.Button(self.window, text="Edit", background='yellow', foreground='black',
                                    width=self.BUTTON_WIDTH,
                                    height=self.BUTTON_HEIGHT, command=partial(self.edit_new_todo, todo_item))

            remove_button = tk.Button(self.window, text='Remove', background='red', foreground='black', width=self.BUTTON_WIDTH,
                                      height=self.BUTTON_HEIGHT, command=partial(self.remove_item, self.todo_list, todo_item))

            y_pos = 200 + (30 * count)
            task_name_label.place(x=50, y=y_pos)
            task_priority_label.place(x=400, y=y_pos)
            remove_button.place(x=630, y=y_pos)
            edit_button.place(x=800, y=y_pos)
            count += 1
        # run tkinter main event loop
        self.window.mainloop()

    def create_new_todo(self):
        self.popup = tk.Tk()
        self.popup.title("Enter new To do item details")
        self.popup.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        todo_title = tk.Label(self.popup, text='Task Name', foreground='black', width=30, height=2)
        todo_title.pack()
        self.todo_title_entry = tk.Entry(self.popup)
        self.todo_title_entry.pack()
        todo_priority = tk.Label(self.popup, text='Priority', foreground='black', width=30, height=2)
        todo_priority.pack()
        self.todo_priority_entry = tk.Entry(self.popup)
        self.todo_priority_entry.pack()

        add_button = tk.Button(self.popup, text="Add New ToDo", background='green', foreground='white', width=self.BUTTON_WIDTH,
                               height=self.BUTTON_HEIGHT, command=self.submit_new_todo)

        add_button.pack()
        self.popup.mainloop()

    def edit_new_todo(self, todo_item):
        self.popup = tk.Tk()
        self.popup.title("Edit Todo Item")
        self.popup.geometry(f'{self.WIDTH}x{self.HEIGHT}+{self.X_POS}+{self.Y_POS}')
        todo_title = tk.Label(self.popup, text='Task Name', foreground='black', width=30, height=2)
        todo_title.pack()
        self.todo_title_entry = tk.Entry(self.popup)
        self.todo_title_entry.pack()
        todo_priority = tk.Label(self.popup, text='Priority', foreground='black', width=30, height=2)
        todo_priority.pack()
        self.todo_priority_entry = tk.Entry(self.popup)
        self.todo_priority_entry.pack()

        add_button = tk.Button(self.popup, text="Edit New ToDo", background='green', foreground='white',
                               width=self.BUTTON_WIDTH,
                               height=self.BUTTON_HEIGHT, command=partial(self.submit_edit_todo, todo_item))

        add_button.pack()
        self.popup.mainloop()

    def submit_new_todo(self):
        new_task_title = self.todo_title_entry.get()
        new_task_priority = self.todo_priority_entry.get()
        new_task_priority = int(new_task_priority)
        new_task = Task(new_task_title, new_task_priority)
        self.todo_list.add_task(new_task)
        self.popup.destroy()
        self.create_render_main_screen()

    def submit_edit_todo(self, todo_item):
        edit_task_title = self.todo_title_entry.get()
        edit_task_priority = self.todo_priority_entry.get()
        edit_task_priority = int(edit_task_priority)
        edit_task = Task(edit_task_title, edit_task_priority)
        self.todo_list.update_task(todo_item, edit_task)
        self.popup.destroy()
        self.create_render_main_screen()



    def remove_item(self, tdl, todo_item):
        tdl.remove_task(todo_item)
        self.refresh()

    def refresh(self):
        self.window.destroy()
        self.__init__(self.todo_list.tasks)





# initialize main window
if __name__ == '__main__':
    App()




