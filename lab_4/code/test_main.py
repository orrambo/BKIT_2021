import unittest
from unittest.mock import patch, Mock
from main import get_roots, check
import math

class TestRoots(unittest.TestCase):

    def test_roots_is_equal(self):
        self.assertEqual(get_roots(1,-5,6), [-1.732, 1.732, -1.414, 1.414])
        self.assertEqual(get_roots(1,-4,4), [-1.414, 1.414])
        self.assertEqual(get_roots(-4,16,0), [0.0, -2.0, 2.0])
        self.assertEqual(get_roots(1,0,-16), [-2.0, 2.0])

    def test_string_root(self):
        self.assertRaises(TypeError, get_roots, 'fafsdlkfj')
        self.assertRaises(TypeError, get_roots, 'True')
        self.assertRaises(TypeError, get_roots, [1,2])

    # @patch.object(get_roots, 'check')
    # def test_get_roots(self, mock_check):
    #     mock_check.assert_called()

if __name__ == '__main__':
    unittest.main()