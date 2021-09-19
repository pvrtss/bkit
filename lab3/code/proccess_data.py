import sys
import json
from lab_python_fp import cm_timer_1, Unique, field, print_result, gen_random

'''
try:
    path = sys.argv[1]
except IndexError:
    print("Не указан путь к файлу. Попробуйте ещё раз.")
else:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
'''

path = sys.argv[1]

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(lst):
    return sorted(list(Unique(field(lst, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(lst):
    return list(filter(lambda s: str.startswith(str.lower(s), 'программист'), lst))

@print_result
def f3(lst):
    return list(map(lambda s: s + " c опытом Python", lst))

@print_result
def f4(lst):
    return list(zip(lst, list('зарплата {} руб.'.format(num) for num in gen_random(len(lst), 100000, 200000))))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))