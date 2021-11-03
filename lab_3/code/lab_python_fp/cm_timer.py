from contextlib import contextmanager
import time

class cm_timer_1():

    def __init__(self, before_mes, after_mes):
        self.before_mes = before_mes
        self.after_mes = after_mes
        self.start_time = None
        
    def __enter__(self):
        print('Основа - класс')
        print(self.before_mes)
        self.start_time = time.time()
        return 'Важная информация'
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(f'Время работы менеджера: {time.time() - self.start_time} сек')
            print(self.after_mes)

@contextmanager
def cm_timer_2(before_mes, after_mes):
    print('Основа - библиотека contextlib')
    print(before_mes)
    start_time = time.time()
    yield 333
    print(f'Время работы менеджера: {time.time() - start_time} сек')
    print(after_mes)

if __name__ == '__main__':
    before_mes = 'Контекстный менеджер начал свою работу'
    after_mes = 'Контекстный менеджер закончил свою работу\n'

    with cm_timer_1(before_mes, after_mes):
        time.sleep(2)
    with cm_timer_2(before_mes, after_mes):
        time.sleep(3)

