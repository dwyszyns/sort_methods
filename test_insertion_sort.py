import random
import unittest
from insertion_sort import insertionSort


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        self.assertEqual(insertionSort(arr), [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(insertionSort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(insertionSort(arr), [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = random.sample(range(100), 10)
        self.assertEqual(insertionSort(arr), sorted(arr))

    def test_list_with_duplicates(self):
        arr = [1, 2, 3, 2, 1]
        self.assertEqual(insertionSort(arr), [1, 1, 2, 2, 3])

    def test_list_with_negative_numbers(self):
        arr = [-5, 0, 3, -2, 1]
        self.assertEqual(insertionSort(arr), [-5, -2, 0, 1, 3])


if __name__ == '__main__':
    unittest.main()
