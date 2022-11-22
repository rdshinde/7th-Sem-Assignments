# Knapsack using greedy approach
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