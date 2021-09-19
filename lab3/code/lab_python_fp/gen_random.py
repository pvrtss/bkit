import random

def gen_random(amount, begin, end):
    for i in range(amount):
        yield random.randint(begin, end)

if __name__ == '__main__':
    for i in gen_random(5, 1, 10):
        print(i)
