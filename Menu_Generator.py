# Final project for Python Programming course by https://www.borntodev.com/
# This is a food generator that randomizes Thai Street Food.

##-----------------------------------------##

import random
from tkinter import *

# Read data file.
list_type = "data_type.txt"
with open(list_type, "r", encoding='utf-8') as file_type:
    type_data_lines = file_type.read().splitlines()
    type_data = set(type_data_lines) # Make as set because don't want the duplicate data

list_meat = "data_meat.txt"
with open(list_meat, "r", encoding='utf-8') as file_meat:
    meat_data_lines = file_meat.read().splitlines()
    meat_data = set(meat_data_lines)

##-----------------------------------------##

def type_random():
    food_type = random.choice(list(type_data))
    type_result.configure(text=food_type)

def meat_random():
    meat_type = random.choice(list(meat_data))
    meat_result.configure(text=meat_type)

#def add_menu():
#   typeAdd = input("Enter New Type: ")
#   list_type.append(typeAdd)
#   meatAdd = input("Enter New Meat:")
#   list_meat.append(meatAdd)

##-----------------------------------------##

# Main Window GUI
MainWindow = Tk()
MainWindow.title("Menu Generator")
MainWindow.geometry("250x135")

head_message = Label(MainWindow,text="ตามสั่งอะไรดี?", font=("Chakra Petch",14))
head_message.place(x="70", y="0.5")
type_text = Label(MainWindow,text="Type : ", font=("Roboto",12), width="7")
type_text.place(x="15", y="35")
type_result = Label(MainWindow,text="", font=("Chakra Petch",13), bg="#FFDA95", width="15")
type_result.place(x="80", y="35")
meat_text = Label(MainWindow,text="Meat : ", font=("Roboto",12), width="7")
meat_text.place(x="15", y="65")
meat_result = Label(MainWindow,text="", font=("Chakra Petch",13), bg="#ffda95", width="15")
meat_result.place(x="80", y="65")

Random_Button = Button(MainWindow, text ="Random!", font=("Roboto",10), command =lambda:[type_random(),meat_random()]
                       , width="12", bg="#6495ED")
Random_Button.place(x="30", y="100")
Add_Button = Button(MainWindow, text="Add Menu", font=("Roboto",10), width="12", bg="#9a8bf2")
Add_Button.place(x="130", y="100")

MainWindow.mainloop()