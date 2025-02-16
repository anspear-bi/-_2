# -*- coding: utf-8 -*-
"""
2.2
"""
def split_country_name(country_name):
    words = country_name.split()
    for word in words:
        print(word)

country_name = input("Введите название страны (состоящее из двух слов): ")
split_country_name(country_name)

