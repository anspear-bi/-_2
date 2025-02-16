# -*- coding: utf-8 -*-
"""
2.5
"""
def calculate_profit(sales):
    profit_percentage = 0.19
    return sales * profit_percentage

sales_amount = float(input("Введите плановую сумму общего объема продаж: "))
profit = calculate_profit(sales_amount)

print(f"Прибыль, которая будет получена: {profit:.2f} рублей")

