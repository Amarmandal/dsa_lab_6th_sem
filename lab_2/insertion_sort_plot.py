import matplotlib.pyplot as plt
import numpy as np
import time
import random
from insertion_sort import insertionSort


input_sizes = range(100, 2000, 10)

insertion_best_case_time = []
# insertion_worst_case_time = []
# insertion_avg_case_time = []

def case_insertion_sort(inputSeq):
    start_time = time.time()
    insertionSort(inputSeq)
    end_time = time.time()
    diff = ( end_time - start_time) * 1000
    return diff

# for insertion sort
for i in input_sizes:
    #creating list of number but in reverse order
    # worst_case_values = np.arange(i, 0, -1)
    #creating a list of number having length i
    best_case_values = np.arange(0, i)
    #creating a list of number having length i + shuffling element
    # avg_case_values = np.arange(0, i)
    # random.shuffle(avg_case_values)

    #timing of different cases
    
    best_time_in_ms = case_insertion_sort(best_case_values)
    # avg_time_in_ms = case_insertion_sort(avg_case_values)
    # worst_time_in_ms = case_insertion_sort(worst_case_values)

    #append list of time for plotting
    insertion_best_case_time.append(best_time_in_ms)
    # insertion_worst_case_time.append(worst_time_in_ms)
    # insertion_avg_case_time.append(avg_time_in_ms)

plt.plot(input_sizes, insertion_best_case_time, ".", label="Best Case")
# plt.plot(input_sizes, insertion_worst_case_time, "*", label="Worst Case")
# plt.plot(input_sizes, insertion_avg_case_time, "+", label="Average Case")
plt.xlabel("Input size")
plt.ylabel("Time in miliseconds")
plt.title("Insertion Sort")
plt.legend()

plt.show()

