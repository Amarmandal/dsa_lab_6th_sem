import matplotlib.pyplot as plt
import time
from binary_search import binary_search
from linear_search import linear_search


input_sizes = range(100, 100000, 10)
linear_best_case_time = []
linear_worst_case_time = []

binary_best_case_time = []
binary_worst_case_time = []

def case_binary_search(no_of_inputs, target):
    start_time = time.time()
    binary_search(range(no_of_inputs), 0, no_of_inputs - 1, target)
    end_time = time.time()
    diff = ( end_time - start_time) * 1000
    return diff

def case_linear_search(no_of_inputs, target):
    start_time = time.time()
    linear_search(range(no_of_inputs), target)
    end_time = time.time()
    diff = ( end_time - start_time) * 1000
    return diff

# for linear search
for i in input_sizes:
    best_time_in_ms = case_linear_search(i, 0)
    worst_time_in_ms = case_linear_search(i, i)
    linear_best_case_time.append(best_time_in_ms)
    linear_worst_case_time.append(worst_time_in_ms)

# for binary search
for j in input_sizes:
    best_time_in_ms = case_binary_search(j, (j - 1) // 2)
    worst_time_in_ms = case_binary_search(j, j)
    binary_best_case_time.append(best_time_in_ms)
    binary_worst_case_time.append(worst_time_in_ms)

fig, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)

plt1.plot(input_sizes, linear_best_case_time, ".", label="Best Case")
plt1.plot(input_sizes, linear_worst_case_time, "*", label="Worst Case")
plt1.set_xlabel("Input size")
plt1.set_ylabel("Time in miliseconds")
plt1.set_title("Linear Search")
plt1.legend()


#binary search
plt2.plot(input_sizes, binary_best_case_time, ".", label="Best Case")
plt2.plot(input_sizes, binary_worst_case_time, "*", label="Worst Case")
plt2.set_xlabel("Input size")
plt2.set_ylabel("Time in miliseconds")
plt2.set_title("Binary Search")
plt2.legend()
plt.show()

def worst_case_linear_search(worst_case_value):
    start_time = time.time()
    linear_search(range(100), worst_case_value)
    end_time = time.time()
    diff = (start_time - end_time) * 1000

print(case_linear_search(1000))