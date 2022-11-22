from figurecolor import *
import math

class Circle():
    def __init__(self,radius=5, color=FigureColor()):
        self.__radius = radius
        self.__color = color
        self.__area = math.pi*radius*radius

    def __repr__(self):
        return f"Круг площадью {self.__area}, цвет: {str(self.__color)}"
