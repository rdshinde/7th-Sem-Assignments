# Fibonacci numbers using dynamic programming

```python
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
```
### Driver code
```python
n = 9
print(fibonacci(n))
```
# Fibonacci numbers using recursion

```python
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

```
### Driver code
```python
n = 9
print(fibonacci(n))
```

# GCD using recursion
```python
def findGCD(x, y):
    if y == 0:
        return x
    else:
        return findGCD(y, x % y)
```
# GCD using iteration
```python
def findGCD2(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
```

# Job Scheduling alogrithm
```python
def jobScheduling(jobs, n):
    # Sort the jobs according to their finish time
    jobs.sort(key = lambda x: x[1])

    # To store the selected jobs
    selectedJobs = []

    # Select the first job
    selectedJobs.append(jobs[0])

    # Iterate through the remaining jobs
    for i in range(1, n):
        # If the start time of the current job is greater than or equal to the finish time of the previously selected job, then select the current job
        if jobs[i][0] >= selectedJobs[-1][1]:
            selectedJobs.append(jobs[i])

    # Print the selected jobs
    for job in selectedJobs:
        print(job[2], end = " ")
```
### Driver code
```python
jobs = [[1, 2, 'a'], [3, 5, 'b'], [0, 6, 'c'], [5, 7, 'd'], [5, 9, 'e'], [7, 8, 'f']]
n = len(jobs)
jobScheduling(jobs, n)
```

# 0-1 Knapsack using dynamic programming
```python
def knapSack(W, wt, val, n):
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
print(knapSack(W, wt, val, n))
i = n
j = W
while i > 0 and j > 0:
    if K[i][j] != K[i-1][j]:
        print("item", i, "is taken")
        j = j - wt[i-1]
    i = i - 1
```

# Knapsack using greedy approach
```python
from typing import ItemsView
def knapsackUsingGreedy(items, capacity):
    # Sort items by value/weight ratio
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    totalValue = 0.0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            totalValue += item.value
        else:
            fraction = capacity / item.weight
            totalValue += item.value * fraction
            break

    return totalValue

def main():
    # Read input
    capacity, n = map(int, input().split())
    items = []
    for i in range(n):
        value, weight = map(int, input().split())
        items.append(ItemsView(value, weight))

    # Compute the maximum value of fractions of items that fit into the knapsack
    maxValue = knapsackUsingGreedy(items, capacity)
    print("{:.3f}".format(maxValue))

if __name__ == "__main__":
    main()
```
# matrix multiplication using threading
```python
import threading

def matrixMultiplicationUsingThreading(matrix1, matrix2, result, row, col):
    result[row][col] = 0
    for i in range(len(matrix1[0])):
        result[row][col] += matrix1[row][i] * matrix2[i][col]


def matrixMultiplication(matrix1, matrix2):
    result = [[0 for i in range(len(matrix2[0]))] for j in range(len(matrix1))]
    threads = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            thread = threading.Thread(target=matrixMultiplicationUsingThreading, args=(
                matrix1, matrix2, result, i, j))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    return result

# Driver code
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrixMultiplication(matrix1, matrix2)
for row in result:
    print(row)
```
# N Queen Problem
```python
# Python program to solve N Queen
# Problem using backtracking

global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def isSafe(board, row, col):
    
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
    
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False
    
        # Check lower diagonal on left side
        for i, j in zip(range(row, N, 1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False
    
        return True

def solveNQUtil(board, col):
        
            # base case: If all queens are placed
            # then return true
            if col >= N:
                return True
        
            # Consider this column and try placing
            # this queen in all rows one by one
            for i in range(N):
        
                if isSafe(board, i, col):
                    
                    # Place this queen in board[i][col]
                    board[i][col] = 1
        
                    # recur to place rest of the queens
                    if solveNQUtil(board, col + 1) == True:
                        return True
        
                    # If placing queen in board[i][col
                    # doesn't lead to a solution, then
                    # queen from board[i][col]
                    board[i][col] = 0
        
            # if the queen can not be placed in any row in
            # this colum col then return false
            return False

# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s. Note that
# there may be more than one solutions, this
# function prints one of the feasible solutions.
def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
            ]
    
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False
    
    printSolution(board)
    return True

# Driver Code
solveNQ()
```
# Tower of hanoi
```python
def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    towerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    towerOfHanoi(n-1, auxiliary, destination, source)


# Driver code
n = 4
towerOfHanoi(n, 'A', 'C', 'B')
```
# Travelling Salesman Problem using Dynamic Programming
```python
import itertools
def travellingSalesman(graph, s):
    n = len(graph)
    # All subsets of vertices other than source
    subsets = []
    for i in range(1, n):
        for subset in itertools.combinations(range(1, n), i):
            if 0 not in subset:
                subsets.append(list(subset))
    # Initialize all subsets with infinity
    dist = {}
    for subset in subsets:
        dist[tuple(subset)] = float('inf')
    # Distance from source to itself is 0
    for i in range(1, n):
        dist[(i,)] = graph[s][i]
    # Iterate over all subsets
    for size in range(2, n):
        for subset in subsets:
            if len(subset) == size:
                # Find minimum distance from previous subsets
                for i in subset:
                    subsetWithoutI = list(subset)
                    subsetWithoutI.remove(i)
                    val = dist[tuple(subsetWithoutI)] + graph[i][subset[0]]
                    if val < dist[tuple(subset)]:
                        dist[tuple(subset)] = val
    # Calculate minimum distance from last subset to source
    minDist = float('inf')
    for i in range(1, n):
        val = dist[tuple(subset)] + graph[i][0]
        if val < minDist:
            minDist = val
    return minDist


# Driver code
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(travellingSalesman(graph, s))
```

# Merge Sort
```python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)
```

# Quick Sort
```python
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)
print(arr)
```