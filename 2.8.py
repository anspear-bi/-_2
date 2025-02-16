# -*- coding: utf-8 -*-
"""
2.8
"""
def calculate_candies(n, m):
    return m // (n + 1)  # Делим на количество друзей плюс Буратино

# Ввод данных
input_data = input("Введите количество друзей (N) и общее количество конфет (M) через пробел: ")
n, m = map(int, input_data.split())

candies_per_person = calculate_candies(n, m)

print(candies_per_person)

