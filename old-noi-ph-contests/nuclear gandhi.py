from itertools import combinations
t = int(input())

for i in range(t):
    n, b = [int(x) for x in input().split()]
    if len(list(combinations(list(range(1, n + 1)), 2))) - b <= 0:
        print(255)
    else:
        if len(list(combinations(list(range(1, n + 1)), 2))) - b == n:
            print(1)
        else:
            print(len(list(combinations(list(range(1, n + 1)), 2))) - b)
# 4 islands have 6 bridges.
# If there are 6 bridges and you take away 2, there would be 4 bridges left.
# You can get a maximum of 1 cultural sphere since there are 4 bridges and 4 islands.
# If the remaining bridges is equal to the number of islands, print 1.