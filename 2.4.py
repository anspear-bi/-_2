# -*- coding: utf-8 -*-
"""
2.4
"""
def total_entities():
    # Количество жён
    wives = 7
    # Количество мешков у каждой жены
    bags_per_wife = 7
    # Количество кошек в каждом мешке
    cats_per_bag = 7
    # Количество котят у каждой кошки
    kittens_per_cat = 7
    
    # Общее количество кошек
    total_cats = wives * bags_per_wife * cats_per_bag
    # Общее количество котят
    total_kittens = total_cats * kittens_per_cat
    
    # Общее количество людей и животных
    total = 1 + wives + total_cats + total_kittens  # 1 - это тот, кто идет в Сент-Айвс
    
    return total

print("Общее количество людей и животных, направляющихся в Сент-Айвс:", total_entities())

