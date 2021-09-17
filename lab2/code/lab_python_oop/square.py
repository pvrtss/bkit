from .rectangle import Rectangle

class Square(Rectangle):
    
    FIGURE_TYPE = "Квадрат"

    def __init__(self, length, color):
        '''
        Конструктор

        Args:
            length (int): Длина стороны квадрата
            color (str): Цвет
        '''
        super().__init__(length, length, color)

    def __repr__(self):
        return '{} {} цвета с длиной стороны {} площадью {}.'.format(
            Square.get_figure_type(),
            self.color.colorproperty,
            self.height,
            self.area()
        )

    