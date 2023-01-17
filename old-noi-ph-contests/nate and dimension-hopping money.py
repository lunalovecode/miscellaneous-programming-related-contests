n, x, y = [int(x) for x in input().split()]
def percentage(percent, whole):
    return 100 * (percent/whole)
mon = n
tues = mon + percentage(y, mon)
wed = tues - percentage(x, tues)
thurs = wed - percentage(y, wed)
fri = thurs
print(mon, tues, wed, thurs, fri)