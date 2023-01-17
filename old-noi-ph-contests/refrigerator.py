t = int(input())
n = int(input())

def count_odds(lst):
    c = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            c += 1
    return c

for j in range(t):
    lst = [int(x) for x in input().split()]
    print(count_odds(lst))Q