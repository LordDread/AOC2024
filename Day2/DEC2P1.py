with open('input.txt') as f:
    lines = f.read().splitlines()

def reportSearch (increase, line):
    lastValue = int(line[0])
    for n in range(1, len(line)):
        if increase:
            if lastValue - int(line[n]) < -3 or lastValue - int(line[n]) > -1:
                return False
        elif not increase:
            if lastValue - int(line[n]) > 3 or lastValue - int(line[n]) < 1:
                return False
        lastValue = int(line[n])
    return True


counter = 0
for each in lines:
    line = each.split()
    if int(line[0]) < int(line[1]) and int(line[0]) - int(line[1]) >= -3:
        increase = True
    elif int(line[0]) > int(line[1]) and int(line[0]) - int(line[1]) <= 3:
        increase = False
    else:
        continue
    if reportSearch(increase, line):
        counter= counter + 1
print(counter)