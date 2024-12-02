import bisect
left = []
right = []
total = 0
with open('input.txt') as f:
    for line in f:
        total = total + abs(int(line[0:5]) - int(line[-6:-1]))
        bisect.insort(left,int(line[0:5]))
        bisect.insort(right, int(line[-6:-1]))
print(total)