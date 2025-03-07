import sys
import math

def calc_area(r):
    """Calculo del área de un círculo dado su radio"""
    area = math.pi * r** 2
    return area

# Cálculo del área del círculo
radius = 5 
area = calc_area(radius) 
print(f"Area of circle: {area:.2f}")
