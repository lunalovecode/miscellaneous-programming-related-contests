t = int(input())
for i in range(t):
    n, b = [int(x) for x in input().split()]
    if n - b <= 0:
        print(1)
    else:
        print(n - b)