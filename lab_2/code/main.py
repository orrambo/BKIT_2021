from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pandas as pd

n = 11

def main():
    r = Rectangle("синий", n, n)
    c = Circle("зеленый", n)
    s = Square("красный", n)

    table = pd.DataFrame(
        {
            "Тип фигуры": [
                Rectangle.get_figure_type(),
                Circle.get_figure_type(),
                Square.get_figure_type(),
            ],
            "Цвет": [
                r.fc.colorproperty, c.fc.colorproperty, s.fc.colorproperty,
            ],
            "Ширина": [
                r.width, '0' , s.width,
            ],
            "Длина": [
                r.height, '0' , s.height,
            ],
            "Радиус": [
                '0', c.r, '0',
            ],
            "Площадь": [
                round(r.square(), 2), round(c.square(), 2) , round(s.square(), 2),
            ]
        }
    )

    print(table)

if __name__ == "__main__":
    # execute only if run as a script
    main()