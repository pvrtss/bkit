from abc import ABC, abstractmethod

class Shape(ABC):
    
    FIGURE_TYPE = None

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    
    @abstractmethod
    def area(self):
        pass
