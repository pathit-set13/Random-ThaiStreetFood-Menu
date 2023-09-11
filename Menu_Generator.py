# Final project for Python Programming course by https://www.borntodev.com/
# This is a food generator that randomizes Thai Street Food.
import random
from tkinter import *

def type_random():
    list_type = ["ผัดกะเพรา", "ผัดพริกแกง", "คั่วพริกเกลือ", "สุกี้น้ำ", "สุกี้แห้ง", "ข้าวผัด", "ผัดผงกะหรี่",
                 "ทอดกระเทียม", "ผัดน้ำมันหอย", "ผัดคะน้า"]
    food_type = random.choice(list_type)
    label_type.configure(text=food_type)


def meat_random():
    list_meat = ["หมู", "หมูกรอบ", "หมูสับ", "ไก่", "เนื้อ", "หมึก", "กุ้ง", "ปลาดุก", "ปลาสลิด", "ทะเลรวม"]
    meat_type = random.choice(list_meat)
    label_meat.configure(text=meat_type)

#def add_menu():
#   typeAdd = input("Enter New Type: ")
#   list_type.append(typeAdd)
#   meatAdd = input("Enter New Meat:")
#   list_meat.append(meatAdd)

MainWindow = Tk()
MainWindow.geometry("350x125")
label_message = Label(MainWindow,text="What should to eat?", font=("Roboto",14))
label_message.grid(row=0, column=1)
label_typetext = Label(MainWindow,text="Menu Type : ", font=("Roboto",12))
label_typetext.grid(row=1, column=0)
label_type = Label(MainWindow,text="", font=("Chakra Petch",12), bg="#ffda95", width="15")
label_type.grid(row=1, column=1)
label_meattext = Label(MainWindow,text="Meat : ", font=("Roboto",12))
label_meattext.grid(row=2, column=0)
label_meat = Label(MainWindow,text="", font=("Chakra Petch",12), bg="#ffda95", width="15")
label_meat.grid(row=2, column=1)
Random_Button = Button(MainWindow, text = "Random!", command = lambda:[type_random(),meat_random()])
Random_Button.grid(row = 3, column = 1)

MainWindow.mainloop()



#type_random()
#meat_random()