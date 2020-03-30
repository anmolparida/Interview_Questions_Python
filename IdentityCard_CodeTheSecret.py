

# Secret information is:
#
# The identity card should start with digit 2, 6, 9. [Done]
# It must contain exactly 12 digits. [Done]
# It must contain only digits from (0-9).
# It must not have more than three repeated consecutive digits.
# It may have digits in a group of four separated by one hyphen “-” and other separators are not allowed.


input1 = '1358-1369-1695' #fake
input2 = '3456-7891-2314' #fake
input3 = '234567341234' #real

idNumber = input1

def consecutiveIntegers(number):
    for i in range(1, len(number)):
        if int(number[i]) - int(number[i-1]) == 1:
            return False
        else:
            flag = True
    if flag:
        return  True


countReal = 0


if len(idNumber) == 12:
    countReal = countReal + 1
    if consecutiveIntegers(idNumber) is True:
        countReal = countReal + 1
    else:
        print('Fake')
        exit()


elif len(idNumber) == 14:
    if idNumber[4] == '-' and idNumber[9] == '-':
        countReal = countReal + 1
        idNumber = str(idNumber)
        idNumber = idNumber.replace('-','')
        if consecutiveIntegers(idNumber) is True:
            countReal = countReal + 1
        else:
            print('Fake')
            exit()
    else:
        print('Fake')
        exit()
else:
    print('Fake')
    exit()

for letter in idNumber:
    if letter.isdigit() :
        countReal = countReal + 1
    else:
        print('Fake')
        exit()

if idNumber[0:1] in [2,6,9]:
    countReal = countReal + 1
else:
    print('Fake')
    exit()

print('Real')

