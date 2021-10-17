def field(dicts, *keys):
    
    assert len(keys) > 0
    
    if len(keys) == 1:
        for d in dicts:
            val = d.get(keys[0])
            if val != None:
                yield val
    else:
        for d in dicts:
            res_dict = dict()
            for key in keys:
                val = d.get(key)
                if val != None:
                    res_dict[key] = val
            if len(res_dict) != 0:
                yield res_dict
                
if __name__ == '__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    ls1 = list()
    ls2 = list()

    for i in field(goods, 'title'):
        ls1.append(i)
    print(str(ls1))
    print()

    for i in field(goods, 'title', 'price'):
        ls2.append(i)
    print(ls2)