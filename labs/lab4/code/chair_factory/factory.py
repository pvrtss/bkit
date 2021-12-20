from abc import ABC, abstractmethod


class Chair(ABC):
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def print_info(self):
        print("Информация о стуле:")
        print("      Вес: " + str(self.weight))
        print("     Цена: " + str(self.cost))

    @abstractmethod
    def print_desc(self):
        pass

    @abstractmethod
    def get_style_name(self):
        pass


class ModernChair(Chair):
    def print_desc(self):
        print("Описание: ")
        print(
            "    Объединяет в себе плавность линий и элементы из разнообразных материалов (стекло, металл и др.). \n    Такая мебель выглядит довольно необычно, импровизационно"
        )

    def get_style_name(self):
        return "modern"


class VintageChair(Chair):
    def print_desc(self):
        print("Описание: ")
        print(
            "    Имеет ярко выраженный античный акцент. Легкость форм, изящность\n    деталей и изысканная простота – основные характеристики мебели в данном стиле"
        )

    def get_style_name(self):
        return "vintage"


class ChairBuilder(ABC):
    @abstractmethod
    def build_chair(self, weight, cost):
        pass


class ModernBuilder(ChairBuilder):
    def building_process(self, weight, cost):
        print("Стул в стиле модерн произведен!")
        return ModernChair(weight, cost)

    def build_chair(self, weight, cost):
        return self.building_process(weight, cost)


class VintageBuilder(ChairBuilder):
    def building_process(self, weight, cost):
        print("Стул в стиле винтаж произведен!")
        return VintageChair(weight, cost)

    def build_chair(self, weight, cost):
        return self.building_process(weight, cost)
