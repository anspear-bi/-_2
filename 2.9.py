# -*- coding: utf-8 -*-
"""
2.9
"""
def calculate_bulls_to_release(n, k):
    return n % k  # Остаток от деления - это количество быков, которых нельзя поделить

# Ввод данных
input_data = input("Введите количество быков (N) и количество семей (K) через пробел: ")
n, k = map(int, input_data.split())

bulls_to_release = calculate_bulls_to_release(n, k)

print(bulls_to_release)

