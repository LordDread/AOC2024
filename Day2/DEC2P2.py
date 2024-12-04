with open('input.txt') as f:
    lines = f.read().splitlines()

def reportSearch (increase, line):
    lastValue = int(line[0])
    failsafe = True
    if increase:
        print("increasing")
    else:
        print("decreasing")
    iterate = iter(line)
    for n in range(1, len(line)):
        if n == len(line) - 1 and failsafe:
            return True
        if increase:
            if lastValue - int(line[n]) < -3 or lastValue - int(line[n]) > -1:
                if n <= len(line) - 2:
                    if -3 <= lastValue - int(line[n + 1]) <= -1 and failsafe:
                        failsafe = False
                        continue
                    if -3 <= int(line[n]) - int(line[n + 1]) <= -1 and failsafe:
                        failsafe = False
                        lastValue = int(line[n])
                        next(iterate)
                        continue
                return False
        elif not increase:
            if lastValue - int(line[n]) > 3 or lastValue - int(line[n]) < 1:
                if n <= len(line) - 2:
                    if 3 >= lastValue - int(line[n + 1]) >= 1 and failsafe:
                        #print("used failsafe1")
                        failsafe = False
                        continue
                    if 3 >= int(line[n]) - int(line[n + 1]) >= 1 and failsafe:
                        failsafe = False
                        #print("used failsafe2")
                        lastValue = int(line[n])
                        next(iterate)
                        continue
                return False
        lastValue = int(line[n])
        #print()
    #print("Safe with " + str(failsafe) + " failsafe")
    return True

counter = 0
for each in lines:
    line = each.split()
    print("---------------------")
    print(line)
    if int(line[0]) == int(line[-1]):
        if int(line[1]) < int(line[-2]):
            increase = True
        elif int(line[1]) > int(line[-2]):
            increase = False
        else:
            print("not safe at all")
            continue
    elif (int(line[0]) < int(line[-1]) or int(line[0]) < int(line[-2])):
        increase = True
    elif (int(line[0]) > int(line[-1]) or int(line[0]) > int(line[-2])):
        increase = False
    else:
        print("not safe at all")
        continue
    if reportSearch(increase, line):
        print("safe")
        counter= counter + 1
    else:
        print("not safe")
print()
print(counter)