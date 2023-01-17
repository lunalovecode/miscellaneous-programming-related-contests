n, m, k = [int(x) for x in input().split()]
friend_groups = [input().split() for x in range(m)]
print(friend_groups)
def connected(everyone, p_1, p_2):
    # M A G I C