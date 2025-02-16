# -*- coding: utf-8 -*-
"""
2.6
"""
def calculate_bmi(weight, height):
    bmi = (weight / (height **2)) * 703
    return bmi

weight = float(input("Введите вес (в фунтах): "))
height = float(input("Введите высоту (в дюймах): "))
bmi = calculate_bmi(weight, height)

print(f"Индекс массы тела (ИМТ): {bmi:.2f}")


