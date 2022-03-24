import unittest
import random

from numpy import insert
from insertion_sort import insertionSort
from merge_sort import mergeSort


class TestSortCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSortCase, self).__init__(*args, **kwargs)
        self.sorted_value = [1, 2, 3, 4, 5]

    def test_insertion_sort_reverse(self):
        reverse_array = [5, 4, 3, 2, 1]
        self.assertListEqual(insertionSort(reverse_array), self.sorted_value)

    def test_insertion_sort_sorted(self):
        self.assertListEqual(insertionSort(self.sorted_value), self.sorted_value)


    def test_insertion_sort_random(self):
        random_value = [1, 2, 3, 4, 5]
        random.shuffle(random_value)
        self.assertListEqual(insertionSort(random_value), self.sorted_value)

    def test_merge_sort_reverse(self):
        reverse_array = [5, 4, 3, 2, 1]
        self.assertListEqual(mergeSort(reverse_array), self.sorted_value)

    def test_merge_sort_sorted(self):
        self.assertListEqual(mergeSort(self.sorted_value), self.sorted_value)

    def test_merge_sort_random(self):
        random_value = [1, 2, 3, 4, 5]
        random.shuffle(random_value)
        self.assertListEqual(mergeSort(random_value), self.sorted_value)


if __name__ == "__main__":
    unittest.main()