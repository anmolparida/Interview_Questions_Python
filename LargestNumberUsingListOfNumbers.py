inputList = [9,56,12,3,54]
inputList = [1,33,9,15,39,54,941,334,923,7,97,999,9,9,9,9]

x = []
y = []
for number in inputList:
    if number == 9:
        y.append(str(number))
    else:
        x.append(str(number))
    x = sorted(x,reverse=True)
print(y + x)

