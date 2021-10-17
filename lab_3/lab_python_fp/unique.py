from .gen_random import gen_random

class Unique(object):
    def __init__(self, items, ignore_case = False, **kwargs):
        self.last = set() 
        self.items = items
        self.registr = ignore_case
        self.kwargs = kwargs

    def __next__(self):
        it =  iter(self.items) 
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise 
            else:
                if self.registr == True and isinstance(current, str):
                    temp = current[:]
                    if temp.lower() not in self.last:
                        self.last.add(temp.lower())
                        return current
                elif current not in self.last:
                    self.last.add(current)
                    return current
      
    def __iter__(self):
        return self

if __name__ == '__main__':
    list1 = ['a', "B", 'c', 'd', 'c',"A", 'b', "C", 'c', 'b']

    print(list(Unique(gen_random(50, 1, 4))))

    print(list(Unique(list1)))

    print(list(Unique(list1, ignore_case = True)))

    # Исходный список 
    print(list1)