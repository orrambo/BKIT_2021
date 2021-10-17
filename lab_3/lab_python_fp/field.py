def field(dicts, *keys):
    assert len(keys) > 0

    if len(keys) == 1:
        for dict in dicts:
            value = dict.get(keys[0])
            if value != 0: yield value 
    else:
        for dict in dicts:
            res_dict = {}
            for key in keys:
                value = dict.get(key)
                if value != 0: res_dict[key] = value
            if len(res_dict) != 0: yield res_dict 

if __name__ == '__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    result_list1, result_list2 = [], []

    result_list1 = [i for i in field(goods, 'title')]
    print(result_list1)

    result_list2 = [i for i in field(goods, 'title', 'price')]
    print(result_list2)

