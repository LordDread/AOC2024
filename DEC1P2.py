import bisect
left = []
right = []
with open('input.txt') as f:
    for line in f:
        bisect.insort(left,int(line[0:5]))
        bisect.insort(right, int(line[-6:-1]))
total = 0

for each in left:
    if each not in right:
        continue
    else:
        total = total + each * (right.count(each))

print(total)