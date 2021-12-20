import sys
import math

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
        coef = float(sys.argv[index])
    except:
        while True:
            try: 
                coef = float(input(prompt))
                break
            except ValueError:
                print("Ошибка! Попробуйте ещё раз...")
    return coef
    
def check(result, root):
    if root == 0.0:
        result.append(root)
    elif root > 0.0:
        result.append(-round(math.sqrt(root), 3))
        result.append(round(math.sqrt(root), 3))

def get_roots(a, b, c):
    result = []
    if a == 0:
        if b != 0:
            root = -c / b
            check(result, root)
        return result
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        check(result, root)
    elif D > 0.0:
        sqrtD = math.sqrt(D)
        root1 = (-b + sqrtD) / (2.0*a)
        root2 = (-b - sqrtD) / (2.0*a)
        check(result, root1)
        check(result, root2)
    return result 


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    if a == b == c == 0.0:
        print('Бесконечное число корней')
    else:
        roots = get_roots(a,b,c)
        len_roots = len(roots)
        if len_roots == 0:
            print('Нет корней')
        elif len_roots == 1:
            print('Один корень: {}'.format(roots[0]))
        elif len_roots == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif len_roots == 3:
            print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
        elif len_roots == 4:
            print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    
if __name__ == "__main__":
    main()
