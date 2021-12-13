from abc import ABC, abstractmethod

class Chair(ABC):
    def __init__(self, weight, cost):
        self.weight=weight
        self.cost=cost
    
    def print_info(self):
        print("Информация о стуле:")
        print("      Вес: " + str(self.weight))
        print("     Цена: " + str(self.cost))

    @abstractmethod
    def print_desc(self):
        pass


class ModernChair(Chair):
    def print_desc(self):
        print("Описание: ")
        print("    Объединяет в себе плавность линий и элементы из разнообразных материалов (стекло, металл и др.). \n    Такая мебель выглядит довольно необычно, импровизационно")

class VintageChair(Chair):
    def print_desc(self):
        print("Описание: ")
        print("    Имеет ярко выраженный античный акцент. Легкость форм, изящность деталей и изысканная простота – основные характеристики мебели в данном стиле")

class ChairBuilder(ABC):

    @abstractmethod
    def build_chair(self, weight, cost):
        pass

class ModernBuilder(ChairBuilder):
    def build_chair(self, weight, cost):
        print("Стул в стиле модерн произведен!")
        return ModernChair(weight,cost)

class VintageBuilder(ChairBuilder):
    def build_chair(self, weight, cost):
        print("Стул в стиле винтаж произведен!")
        return VintageChair(weight,cost)