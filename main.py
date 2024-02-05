from merge_sort import mergeSort
from insertion_sort import insertionSort
from qsort import Qsort
from selection_sort import selectionSort
import string
import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)  # set the recursion limit to 10000

if len(sys.argv) < 2:
    sys.exit("Wrong params, Correct usage: python3 main.py filename, max_words")

with open(sys.argv[1], "r") as f:
    starting_list_2 = []
    list_temp = []
    for line in f:
        for word in line.split():
            list_temp.append(word.translate(string.punctuation))
    for i in range(0, int(sys.argv[2]), 100):
        for words in range(0, i):
            if i > len(list_temp):
                break
            starting_list_2.append(list_temp[words])

        starting_list_copy = starting_list_2.copy()
        sort_functions = [mergeSort, Qsort, insertionSort, selectionSort]
        colors = ['r', 'b', 'y', 'm']
        sort_times = []

        for sort_func, color in zip(sort_functions, colors):
            time_start = time.time()
            sort_func(starting_list_copy)
            sort_times.append(time.time() - time_start)

        for time_, color in zip(sort_times, colors):
            plt.plot(i, time_, color + 'o')

        plt.xlabel("Len")
        plt.ylabel("Sort time (s)")
        print(i)
        starting_list_2.clear()

plt.legend([
            'merge_sort',
            'quick_sort',
            'insertion_sort',
            'selection_sort',
            ], loc='upper left')
plt.show()
