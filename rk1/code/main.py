# используется для сортировки
from operator import itemgetter
 
class Language:
    """Язык программирования"""
    def __init__(self, id, title, creator, tool_id):
        self.id = id
        self.title = title
        self.creator = creator
        self.tool_id = tool_id
 
class Tool:
    """Средство разработки"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class LangTool:
    """
    'Язык программирования' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, tool_id, lang_id):
        self.tool_id = tool_id
        self.lang_id = lang_id
 
# Средства разработки
tools = [
    Tool(1, 'Visual Studio'),
    Tool(2, 'XCode'),
    Tool(3, 'Visual Studio Code'),
    Tool(4, 'Netbeans'),
]
 
# Языки программирования
languages = [
    Language(1, 'Python', 'Гвидо ван Россум', 1),
    Language(2, 'C++_ов', 'Бьёрн Страуструп', 2),
    Language(3, 'C', 'Деннис Ритчи', 3),
    Language(4, 'Pascal_ов', 'Никлаус Вирт', 3),
    Language(5, 'Java', 'Джеймс Гослинг', 4),
]
 
lang_tool = [
    LangTool(1,1),
    LangTool(1,2),
    LangTool(1,3),
    LangTool(2,2),
    LangTool(2,4),
    LangTool(3,1),
    LangTool(3,3),
    LangTool(3,4),
 
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(l.title, l.creator, t.name) 
        for t in tools 
        for l in languages
        if l.tool_id == t.id]
    
    # Соединение данных многие-ко-многим
    many_to_many = [(l.title, l.creator, t.name) 
        for t in tools 
        for l in languages  
        for relation in lang_tool
        if t.id == relation.tool_id and l.id == relation.lang_id]
    
 
    print('Задание Б1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    for res in res_1:
        print(res)
    
    print('\nЗадание Б2')
    res_2 = []
    # Перебираем все средства разработки
    for t in tools:
        # Список языков в средствах разработки
        t_leng = list(filter(lambda i: i[2] == t.name, one_to_many))
        # Если средства разработки не пустые
        if len(t_leng) > 0:
            res_2.append((t.name, len(t_leng)))
    res_2.sort(key=itemgetter(1), reverse=True)
    [print(el) for el in res_2]
 
    print("\nЗадание Б3")
    res_3 = {}
    for l in languages:
        if l.title.endswith("ов"):
            # Ищем средства разработки конкретного языка
            l_tools = list(filter(lambda x: x[0] == l.title, many_to_many))
            # Получаем их названия
            l_tools_names = [x[2] for x in l_tools]
            res_3[l.title] = l_tools_names
    [print(k, v) for k, v in res_3.items()]
 
if __name__ == '__main__':
    main()
