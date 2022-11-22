from figurecolor import *
from rectangle import *


class Square(Rectangle):

  def __init__(self, side=6, color=FigureColor()):
    super().__init__(side, side, color)

  def __repr__(self):
    ar1 = super().get_area()
    co1 = super().get_area()
    return f"Квадрат площадью {ar1}, цвет: {str(co1)}"
