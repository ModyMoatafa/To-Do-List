# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:56:21 2023

@author: PC
"""

class to_do_list():
    def __init__(self, my_list):
        self.my_list = my_list
    
    def add_item(self , new_item):
        self.my_list.append(new_item)
        print("the item has been added successfully\n")
        
    def remove_item(self , t_item):
        self.my_list.remove(t_item)
        print("the item has been removed successfully\n")
    
    def view_all_items(self):
        for i in self.my_list:
            print(f"{i}")
 
tasks_list=[]
obj=to_do_list(tasks_list)

print("1- add a task")
print("2- remove a task")
print("3- display all tasks")



while True:
    choice =input("Enter Your Choice :\n")
    if choice=="1":
        new=input("enter the task you want to add:\n")
        obj.add_item(new)
        print("task added succeessfully")
    elif choice=="2":
        rem=input("enter the task you want to remove:\n")
        obj.remove_item(rem)
        print("task reemovd succeessfully")
    elif choice=="3":
        obj.view_all_items()
      
    else:
        print("wrong input please enter a number from the description")
        