# 0-1 Knapsack using dynamic programming
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
