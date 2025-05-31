import random
import time
from memory_profiler import memory_usage

# input size of data
ARRAY_SIZE=1000000

# recursive implementation of the quicksort algorithm
# uses `middle_match` array since values that match the chosen pivot do not
# need to be sorted
def quicksort(input):
    # if we get an array of size 0 or 1, we have reached
    # a base case in the recursion tree
    if len(input) <= 1:
        return input
    # chose middle value of input as the pivot
    chosen_pivot = input[len(input) // 2]

    # break down into left, middle, and right subarrays based on
    # comparison to the chosen pivot value
    left_array = [x for x in input if x < chosen_pivot]
    middle_match = [y for y in input if y == chosen_pivot]
    right_array = [z for z in input if z > chosen_pivot]
    return quicksort(left_array) + middle_match + quicksort(right_array)

# generate random data based on set input size of ARRAY_SIZE
def generate_random_data():
    out = [random.randint(0, ARRAY_SIZE) for x in range(ARRAY_SIZE)]
    return out

# generate sorted data based on set input size of ARRAY_SIZE
def generate_sorted_data():
    out = list(range(ARRAY_SIZE))
    return out

# generate reversed sorted data based on set input size of ARRAY_SIZE
def generate_reversed_sorted_data():
    out = list(range(ARRAY_SIZE, 0, -1))
    return out

# runs quicksort on the input data and measures the time taken & memory used
def test_quicksort(input_data):
    start_time = time.time()
    mem_usage = memory_usage((quicksort, (input_data,)))
    end_time = time.time()
    print("Time taken: " + str(end_time - start_time) + " seconds")
    print("Memory used: " + str(max(mem_usage) - min(mem_usage)) + " MiB")

if __name__ == "__main__":
    print("Excuting quicksort test for random data")
    data = generate_random_data()
    test_quicksort(data)

    print("Excuting quicksort test for sorted data")
    data = generate_sorted_data()
    test_quicksort(data)

    print("Excuting quicksort test for reversed sorted data")
    data = generate_reversed_sorted_data()
    test_quicksort(data)