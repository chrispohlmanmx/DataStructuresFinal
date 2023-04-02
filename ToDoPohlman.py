"""
* Name : ToDoPohlman.py
* Author: Christopher Pohlman
* Created : 4/2/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 11
* IDE: PyCharm 
* Copyright : This is my own original work 
* based on specifications issued by our instructor
* Description : An app that creates a todo list
*            Input: ADD HERE XXX
*            Output: ADD HERE XXX
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""

class PriorityQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, title, priority):
        if self.isEmpty():
            self.head = Task(title, priority)
        else:
            if self.head.priority > priority:
                newTask = Task(title, priority)
                newTask.next = self.head
                self.head = newTask
            else:
                temp = self.head
                while temp.next:
                    if priority <= temp.next.priority:
                        break
                    temp = temp.next
                newTask = Task(title, priority)
                newTask.next = temp.next
                temp.next = newTask

    def pop(self):
        if self.isEmpty():
            raise Exception("Priority Queue is Empty")
        else:
            temp = self.head
            self.head = self.head.next
            return temp

    def peek(self):
        if self.isEmpty():
            raise Exception("Priority Queue is Empty")
        else:
            return self.head.title

    def display(self):
        display_string = ''
        if self.isEmpty():
            return 'Priority Queue is Empty'
        else:
            temp = self.head
            while temp:
                display_string += f'title: {temp.title} Priority: {temp.priority}\n'
                temp = temp.next
        return display_string

class Task:
    def __init__(self, title, priority_value):
        self._title = title
        self.priorities = [1, 2, 3, 4, 5] #higher number will be higher priority
        self.priority = priority_value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value in self.priorities:
            self._priority = value
        else:
            raise ValueError(f'Given value not in allowed list of priority levels {self.priorities}')


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


class ToDoList:
    def __init__(self, name, tasks: [Task]):
        self.name = name
        self.tasks = tasks
        self.priority_queue = PriorityQueue()
        self.size = len(tasks)

    def isEmpty(self):
        return self.size == 0
    def add_task(self, task: Task):
        self.tasks.append(task)
        self.size += 1

    def update_task(self, task_to_change, new_task):
        update_index = self.tasks.index(task_to_change)
        self.tasks[update_index] = new_task

    def remove_task(self, task_to_remove):
        if self.isEmpty():
            raise Exception(f'{self.name} list is currently empty')

        remove_index = self.tasks.index(task_to_remove)
        del self.tasks[remove_index]
        self.size -= 1

    def __str__(self):
        list_str = ''
        if self.isEmpty():
            return f'{self.name} list is currently empty'
        for task in self.tasks:
            list_str += f'Task[Title={task.title}: Priority={task.priority}], '
        return list_str

