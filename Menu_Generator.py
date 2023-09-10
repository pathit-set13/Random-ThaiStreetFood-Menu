# Final project for Python Programming course by https://www.borntodev.com/
# This is a food generator that randomizes Thai Street Food.
import random
from tkinter import *

def type_random():
    list_type = ["ผัดกะเพรา", "ผัดพริกแกง", "คั่วพริกเกลือ", "ุสุกี้น้ำ", "สุกี้แห้ง", "ข้าวผัด", "ผัดผงกะหรี่",
                 "ทอดกระเทียม", "ผัดน้ำมันหอย"]
    food_type = random.choice(list_type)
    print(food_type)


def meat_random():
    list_meat = ["หมู", "หมูกรอบ", "หมูสับ", "ไก่", "เนื้อ", "หมึก", "กุ้ง", "ปลาดุก", "ปลาสลิด"]
    meat_type = random.choice(list_meat)
    print(meat_type)

#def combined_func():

#def add_menu():
#   typeAdd = input("Enter New Type: ")
#   list_type.append(typeAdd)
#   meatAdd = input("Enter New Meat:")
#   list_meat.append(meatAdd)

MainWindow = Tk()
label_Manu = Label(MainWindow,text="What should to eat?")
label_Manu.grid(row=0, column=1)
Random_Button = Button(MainWindow, text = "Random!", command = lambda:[type_random(),meat_random()] ).grid(row = 2, column = 1)

MainWindow.mainloop()



#type_random()
#meat_random()