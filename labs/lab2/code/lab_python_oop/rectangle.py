from .shape import Shape
from .color import ShapeColor

class Rectangle(Shape):
    
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        '''
        Конструктор

        Args:
            width (int): Ширина прямоугольника
            height (int): Высота прямогульника
            color (str): Цвет
        '''
        self.width = width
        self.height = height
        self.color = ShapeColor()
        self.color.colorproperty = color
    
    def area(self):
        ''' Возвращает площадь прямоугольника'''
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.area()
        )
