from math import pi
from .shape import Shape
from .color import ShapeColor

class Circle(Shape):

    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        '''
        Конструктор

        Args:
            radius (int): Радиус круга
            color (str): Цвет
        '''
        self.name = "Круг"
        self.radius = radius
        self.color = ShapeColor()
        self.color.colorproperty = color 
 
    def area(self):
        ''' Возвращает площадь круга'''
        return pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.color.colorproperty,
            self.radius,
            self.area()
        )

    


