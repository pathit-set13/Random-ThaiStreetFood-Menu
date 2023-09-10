# Final project for Python Programming course by https://www.borntodev.com/
# This is a food generator that randomizes Thai Street Food.
import random
import tkinter

def type_random():
    list_type = ["ผัดกะเพรา", "ผัดพริกแกง", "คั่วพริกเกลือ", "ุสุกี้น้ำ", "สุกี้แห้ง", "ข้าวผัด", "ผัดผงกะหรี่",
                 "ทอดกระเทียม", "ผัดน้ำมันหอย"]
    food_type = random.choice(list_type)
    print(food_type)

def meat_random():
    list_meat = ["หมู", "หมูกรอบ", "หมูสับ", "ไก่", "เนื้อ", "หมึก", "กุ้ง", "ปลาดุก", "ปลาสลิด"]
    meat_type = random.choice(list_meat)
    print(meat_type)

type_random()
meat_random()
