import json
import sys
from lab_python_fp import cm_timer_1, Unique, field, print_result, gen_random

try:
    path = 'C:\Microsoft VS Code\python\lab_3\code\data_light.json'
except IndexError:
    raise ValueError("Не указан путь к файлу.")
else:
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
    return dict(zip(lst, list('зарплата {} руб.'.format(num) for num in gen_random(len(lst), 1000000, 2000000))))

if __name__ == '__main__':
    before_mes = 'Контекстный менеджер начал свою работу'
    after_mes = 'Контекстный менеджер закончил свою работу\n'
    with cm_timer_1(before_mes, after_mes):
        f4(f3(f2(f1(data))))