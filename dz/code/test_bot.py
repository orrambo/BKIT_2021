import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *

test1 = 1
test2 = 2
test3 = 3

class TestGetRoots(unittest.TestCase):
    def test1_bot(self):
        res = summary(queen_albums,queen_albums_price,rhcp_albums,rhcp_albums_price,green_day_albums,green_day_albums_price,test1,test2,test3)
        self.assertEqual("Итоговая сумма заказа = 13600\n", res)
    def test2_bot(self):
        res = summary(queen_albums,queen_albums_price,rhcp_albums,rhcp_albums_price,green_day_albums,green_day_albums_price,test2,test1,test3)
        self.assertEqual("Итоговая сумма заказа = 13700\n", res)

if __name__ == "__main__":
    unittest.main()