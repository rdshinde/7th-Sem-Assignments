# Travelling Salesman Problem using Dynamic Programming

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
