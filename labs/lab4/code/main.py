from chair_factory import ModernBuilder, VintageBuilder

if __name__ == "__main__":
    while True:
        print("Выберите стиль стула для производства: \n    1: Модерн\n    2: Винтаж")
        choice = int(input())
        if choice in [1, 2]:
            print("Введите вес: ")
            weight = int(input())
            print("Введите цену: ")
            cost = int(input())
            print()
            if choice == 1:
                chair = ModernBuilder().build_chair(weight, cost)
            else:
                chair = VintageBuilder().build_chair(weight, cost)
            print()
            chair.print_info()
            print()
            chair.print_desc()
            print()
            print()
        else:
            print("Неверный ввод - повторите попытку.")
            print()
        print("Выберите действие: \n    1: Повторить\n    2: Выход")
        print("\n")
        action = int(input())
        if action == 2:
            break
