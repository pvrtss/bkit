# from gen_random import gen_random

class Unique(object):
    def __init__(self, items, ignore_case = False, **kwargs):
        self.seen = set() 
        self.items = items
        self.ic = ignore_case
        self.kwargs = kwargs

    def __next__(self):
        it =  iter(self.items) 
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise StopIteration 
            else:
                if self.ic == True and isinstance(current, str):
                    temp = current[:]
                    if temp.lower() not in self.seen:
                        self.seen.add(temp.lower())
                        return current
                elif current not in self.seen:
                    self.seen.add(current)
                    return current

    def __iter__(self):
        return self

if __name__ == '__main__':
    lst = ['a', 'b', 'c', 'd', 'c',"A", "B", "C", 'c', 'b', 1, 2, 2, 3, 3, 1, 2, 3, 4]

    # print(list(Unique(gen_random(50, 1, 4))))

    print(list(Unique(lst)))

    print(list(Unique(lst, ignore_case = True)))

    # Исходный список 
    print(lst)