from figurecolor import *

class Rectangle():

    def __init__(self, width=20, height=10, color=FigureColor()):
        self.__width = width
        self.__height = height
        self.__color = color
        self.__area = width * height

    def get_area(self):
        return self.__area

    def get_color(self):
        return self.__color

    def get_repr(self):
        return f"Прямоугольник пощадью {self.__area}, цвет: str({self.__color})"
