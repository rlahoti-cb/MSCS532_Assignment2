In this repository, we implement and compare the quicksort and mergesort sorting algorithms.

In order to capture the memory usage of the function calls to the sorting functions, we use the python3 memory_profiler library. This can be installed by executing the following command:

```
pip3 installl memory_profiler
```

In order to compare these two algorithms, we capture the time taken and the memory used for each sorting function call. Furthermore, the sorting functions are called on different types of input data. We use the following data to compare the algorithms --  random data, sorted data, and reversed sorted data. Each call to a sorting function is called using 1,000,000 elements of sorted, random, or reverse sorted data.

The results are captured in the report writeup.