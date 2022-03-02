import unittest
from binary_search import binary_search
from linear_search import linear_search


# interpreter automatically insert
# __name__ = "__main__" at top


class TestCase(unittest.TestCase):

    def test_linear_search(self):
        values = [1, 2, 3, 4, 5]
        not_equal_flag = -1
        self.assertNotEqual(linear_search(values, 2), not_equal_flag)
        self.assertNotEqual(linear_search(values, 3), not_equal_flag)
        self.assertNotEqual(linear_search(values, 99), not_equal_flag)


    def test_binary_search(self):
        values = [1, 2, 3, 4, 5]
        not_equal_flag = -1
        self.assertNotEqual(binary_search(values, 0, len(values) - 1, 1), not_equal_flag)
        self.assertNotEqual(binary_search(values, 0, len(values) - 1, 3), not_equal_flag)
        self.assertNotEqual(binary_search(values, 0, len(values) - 1, 99), not_equal_flag)


if __name__ == "__main__":
    unittest.main()