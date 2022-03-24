import matplotlib.pyplot as plt
import numpy as np
import time
import random
from merge_sort import mergeSort
from insertion_sort import insertionSort


input_sizes = range(100, 10000, 100)

insertion_best_case_time = []
insertion_worst_case_time = []
insertion_avg_case_time = []

merge_best_case_time = []
merge_avg_case_time = []
merge_worst_case_time = []

def case_merge_sort(inputSeq):
    start_time = time.time()
    mergeSort(inputSeq)
    end_time = time.time()
    diff = ( end_time - start_time) * 1000
    return diff


def case_insertion_sort(inputSeq):
    start_time = time.time()
    insertionSort(inputSeq)
    end_time = time.time()
    diff = ( end_time - start_time) * 1000
    return diff

# for merge sort
for j in input_sizes:
    #creating list of number but in reverse order
    worst_case_values = np.arange(j, 0, -1)
    #creating a list of number having length j
    best_case_values = np.arange(0, j)
    #creating a list of number having length j + shuffling element
    avg_case_values = np.arange(0, j)
    random.shuffle(avg_case_values)

    #timing of different cases
    
    best_time_in_ms = case_merge_sort(best_case_values)
    avg_time_in_ms = case_merge_sort(avg_case_values)
    worst_time_in_ms = case_merge_sort(worst_case_values)

    #append list of time for plotting
    merge_best_case_time.append(best_time_in_ms)
    merge_worst_case_time.append(worst_time_in_ms)
    merge_avg_case_time.append(avg_time_in_ms)

plt.plot(input_sizes, merge_best_case_time, ".", label="Best Case")
plt.plot(input_sizes, merge_worst_case_time, "*", label="Worst Case")
plt.plot(input_sizes, merge_avg_case_time, "+", label="Average Case")
plt.xlabel("Input size")
plt.ylabel("Time in miliseconds")
plt.title("Merge Sort")
plt.legend()

plt.show()



