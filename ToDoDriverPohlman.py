"""
* Name : ToDoDriverPohlman.py
* Author: Christopher Pohlman
* Created : 4/2/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 11
* IDE: PyCharm 
* Copyright : This is my own original work 
* based on specifications issued by our instructor
* Description : driver file to test ToDoPohlman
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""

from ToDoPohlman import ToDoList, Task


def main():
    t1 = Task("Finish Final Project", 5)
    t2 = Task("finish fundamental informatics", 2)

    tasks = [t1, t2]

    list1 = ToDoList("Main", tasks)

    print(list1)
    print(f'Priority queue {list1.display_priority_queue()}')

    list1.remove_task(t2)

    print(list1)

    list1.remove_task(t1)
    print(list1)



if __name__ == '__main__':
    main()