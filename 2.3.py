# -*- coding: utf-8 -*-
"""
2.3
"""
def total_cost(s, r):
    return s + r

costs = input("Введите цены шоколадок S и R через пробел: ")
s, r = map(int, costs.split())
total = total_cost(s, r)

print("Общая стоимость шоколадок:", total, "рублей")

