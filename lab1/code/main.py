import sys
import math

def sign(x):
    '''
    Определение знака числа
    Args:
        x (float): Действительное число
    Returns:
        int: Коэффициент квадратного уравнения
    '''
    return 1 if x > 0 else -1 if x < 0 else 0

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef = float(sys.argv[index])
    except:
        print("Ошибка считывания коэффициента " + prompt[-3] + ". Выполните ввод вручную.")
        while True:
            try:
                coef = float(input(prompt))
            except ValueError:
                print("Ошибка ввода. Введите действительное число")
            else:
                break
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        if a == b == c == 0.0:
             raise ValueError
        try:
            y = -b / (2.0*a)
        except ZeroDivisionError:
            pass
        else:
            if y >= 0:
                root1 = abs(math.sqrt(y))
                result.append(root1)
                if y != 0:
                    root2 = -math.sqrt(y)
                    result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        y = []
        if a == 0:
            if sign(b) != sign(c):
                root1 = abs(math.sqrt(-c/b))
                result.append(root1)
                if c != 0:
                    result.append(-math.sqrt(-c/b))
        else:
            y.append((-b + sqD) / (2.0*a))
            y.append((-b - sqD) / (2.0*a))
        for i in y:
            if i >= 0:
                root1 = abs(math.sqrt(i))
                result.append(root1)
                if i != 0:
                    root2 = -math.sqrt(i)
                    result.append(root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    # Вычисление корней
    try:
        roots = get_roots(a,b,c)
    # Вывод корней
    except ValueError:
        print("x - любое действительное число")
    else:
        len_roots = len(roots)
        if len_roots == 0:
            if a == b == c == 0.0:
                print("x - любое действительное число")
            else:
                print('Нет действительных корней')
        elif len_roots == 1:
            print('Один корень: {}'.format(roots[0]))
        elif len_roots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif len_roots == 3:
            print('Три корня: x1 = {}, x2 = {}, x3 = {}'.format(roots[0], roots[1], roots[2]))
        elif len_roots == 4:
            print('Четыре корня: x1 = {}, x2 = {}, x3 = {}, x4 = {}'.format(roots[0], roots[1], roots[2], roots[3]))

    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
