W = 8
N = 4
wi = [3, 3, 5, 6]
ci = [3, 5, 10, 14]

d = [[0] * (W + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for w in range(1, W + 1):
        if wi[i-1] > w:
            d[i][w] = d[i-1][w]
        else:
            d[i][w] = max(d[i-1][w], d[i-1][w-wi[i-1]]+ci[i-1])

print('\n'.join([' '.join(map(str, d[i])) for i in range(N + 1)]))


# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.

# Returns the maximum value
# with knapsack of W capacity
def unboundedKnapsack(W, n, val, wt):
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]

    ans = 0

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    print(dp)
    return dp[W]


# Driver program
W = 5
val = [10]
wt = [2]
n = len(val)

print(unboundedKnapsack(W, n, val, wt))

# This code is contributed by Anant Agarwal.