n = int(input())
for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    if a * b > c:
        print("World record!")
    elif a * b == c:
        print("Joint world record...")
    else:
        print("Try again next time :(")