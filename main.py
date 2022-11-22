from figurecolor import *
from rectangle import *
from circle import *
from square import *
from triangle import *

def main():
    green = FigureColor (0,1,0)
    print(green)
    rec1 = Rectangle(5, 7, green)
    print (rec1)
    cir1 = Circle (10, FigureColor(0,0,1))
    print (cir1)
    square1 = Square (20, FigureColor(1,1,1))
    print (square1)
    tri1 = Triangle(10,15, FigureColor(0,0,0))
    print (tri1)

if __name__ == "__main__":
    main()
