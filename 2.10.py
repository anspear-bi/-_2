# -*- coding: utf-8 -*-
"""
2.10
"""
def meters_to_miles(meters):
    return meters // 1609  # 1 миля = 1609 метров

# Ввод данных
distance_meters = float(input("Введите расстояние в метрах: "))

full_miles = meters_to_miles(distance_meters)

print(f"Фейт пробежала {full_miles} полных миль.")

