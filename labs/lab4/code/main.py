from chair_factory import ModernBuilder, VintageBuilder, Chair

if __name__ == "__main__":
    while(True):
        print("Выберите стиль стула для производства: \n    1: Модерн\n    2: Винтаж")
        choice = int(input())
        print("Введите вес: ")
        weight = int(input())
        print("Введите цену: ")
        cost = int(input())
        if choice == 1:
            chair = ModernBuilder().build_chair(weight, cost)
            print()
            chair.print_info()
            chair.print_desc()
            print()
        elif choice == 2:
            chair = VintageBuilder().build_chair(weight, cost)
            print()
            chair.print_info()
            chair.print_desc()
            print()
        else:
            print("Неверный ввод - повторите попытку.")
        print()
        print("Выберите действие: \n    1: Повторить\n    2: Выход")
        action = int(input())
        if action == 2:
            break
