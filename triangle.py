class Triangle:
    def __init__(self, sideA, sideB, color):
        self.__sideA = sideA
        self.__sideB = sideB
        self.__color = color
        self.__area = (sideA*sideB)/2

    def __repr__(self):
        return f"Треугольник площадью {self.__area}, цвет: {self.__color}"
