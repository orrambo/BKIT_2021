import unittest
from main import Tool, Language, LangTool, task2, task1, task3

class Test(unittest.TestCase):
    
    def setUp(self):
        
        self.tools = [
        Tool(1, 'Visual Studio'),
        Tool(2, 'XCode'),
        Tool(3, 'Visual Studio Code'),
        Tool(4, 'Netbeans'),
        ]
    
        self.languages = [
            Language(1, 'Python', 'Гвидо ван Россум', 1),
            Language(2, 'C++_ов', 'Бьёрн Страуструп', 2),
            Language(3, 'C', 'Деннис Ритчи', 3),
            Language(4, 'Pascal_ов', 'Никлаус Вирт', 3),
            Language(5, 'Java', 'Джеймс Гослинг', 4),
        ]
        
        self.lang_tool = [
            LangTool(1,1),
            LangTool(1,2),
            LangTool(1,3),
            LangTool(2,2),
            LangTool(2,4),
            LangTool(3,1),
            LangTool(3,3),
            LangTool(3,4),
        ]    
        
    def test_task1(self):
        keys = [
            ('Java', 'Джеймс Гослинг', 'Netbeans'),
            ('Python', 'Гвидо ван Россум', 'Visual Studio'),
            ('C', 'Деннис Ритчи', 'Visual Studio Code'),
            ('Pascal_ов', 'Никлаус Вирт', 'Visual Studio Code'),
            ('C++_ов', 'Бьёрн Страуструп', 'XCode'),
            ]
        self.assertEqual(task1(self.languages, self.tools), keys)

    def test_task2(self):
        keys = [
            ('Visual Studio Code', 2),
            ('Visual Studio', 1),
            ('XCode', 1),
            ('Netbeans', 1),
            ]
        self.assertEqual(task2(self.languages, self.tools), keys)
        
    def test_task3(self):
        keys = {
            "C++_ов": ['Visual Studio', 'XCode'],
            "Pascal_ов": ['XCode', 'Visual Studio Code'],
        }
        self.assertEqual(task3(self.languages, self.tools, self.lang_tool), keys)

if __name__ == '__main__':
    unittest.main()