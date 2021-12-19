from operator import itemgetter


class Musician:
    """Музыкант"""

    def __init__(self, id, fio, salary, orch_id):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.orch_id = orch_id


class Orchestra:
    """Оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class MusOrch:
    """
    'Музыканты оркестра' для реализации
    связи многие-ко-многим
    """

    def __init__(self, orch_id, mus_id):
        self.orch_id = orch_id
        self.mus_id = mus_id


def task_1(orchestras, musicians):
    # Соединение данных один-ко-многим
    one_to_many = [
        (m.fio, m.salary, o.name)
        for o in orchestras
        for m in musicians
        if m.orch_id == o.id
    ]
    return sorted(one_to_many, key=itemgetter(0))

def task_2(orchestras, musicians):
    one_to_many = [
        (m.fio, m.salary, o.name)
        for o in orchestras
        for m in musicians
        if m.orch_id == o.id
    ]
    res = list()
    # Перебираем все оркестры
    for o in orchestras:
        # Список музыкантов в оркестре
        o_mus = list(filter(lambda i: i[2] == o.name, one_to_many))
        # Если оркестр не пустой
        if len(o_mus) > 0:
            res.append((o.name, len(o_mus)))
    return sorted(res, key=itemgetter(1), reverse=True)

def task_3(orchestras, musicians, mus_orch):
    many_to_many = [
        (m.fio, m.salary, o.name)
        for o in orchestras
        for m in musicians
        for relation in mus_orch
        if o.id == relation.orch_id and m.id == relation.mus_id
    ]
    res = dict()
    for m in musicians:
        if m.fio.endswith("ов"):
            # Ищем оркестры конкретного музыканта
            m_orchs = list(filter(lambda x: x[0] == m.fio, many_to_many))
            # Получаем их названия
            m_orchs_names = [x[2] for x in m_orchs]
            res[m.fio] = m_orchs_names
    return res

def main():
    # Оркестры
    orchestras = [
        Orchestra(1, "Electric Light Orchestra"),
        Orchestra(2, "Mariinsky Theatre Orchestra"),
        Orchestra(3, "Moscow Chamber Orchestra"),
        Orchestra(4, "Ukrainian Radio Symphony Orchestra"),
        Orchestra(5, "National Symphony Orchestra of Ukraine"),
    ]

    # Музыканты
    musicians = [
        Musician(1, "Линн", 70000, 1),
        Musician(2, "Тэнди", 67000, 1),
        Musician(3, "Смирнов", 20000, 2),
        Musician(4, "Карпов", 32000, 3),
        Musician(5, "Прокопенко", 14000, 4),
        Musician(6, "Карчук", 12000, 5),
        Musician(7, "Соловьёва", 14000, 3),
    ]

    # Оркестры и музыканты
    mus_orch = [
        MusOrch(1, 1),
        MusOrch(1, 2),
        MusOrch(2, 3),
        MusOrch(3, 4),
        MusOrch(3, 7),
        MusOrch(4, 5),
        MusOrch(5, 6),
        MusOrch(1, 3),
        MusOrch(4, 1),
        MusOrch(2, 4),
        MusOrch(3, 3),
    ]

    print("Задание Б1")
    res_1 = task_1(orchestras, musicians)
    [print(el) for el in res_1]

    print("\nЗадание Б2")
    res_2 = task_2(orchestras, musicians)
    [print(el) for el in res_2]

    print("\nЗадание Б3")
    res_3 = task_3(orchestras, musicians, mus_orch)
    [print(k, v) for k, v in res_3.items()]

if __name__ == "__main__":
    main()
