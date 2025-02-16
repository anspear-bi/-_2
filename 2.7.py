# -*- coding: utf-8 -*-
"""
2.7
"""
def calculate_rain_volume(precipitation_cm, area_hectares):
    liters_per_cm = 10000  # 1 гектар = 10000 м², 1 см = 1 литр на м²
    return precipitation_cm * liters_per_cm * area_hectares

precipitation = 1  # уровень осадков в см
area = 1  # площадь в гектарах

rain_volume = calculate_rain_volume(precipitation, area)

print(rain_volume)

