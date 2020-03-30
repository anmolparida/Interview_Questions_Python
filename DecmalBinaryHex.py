number = '1b2A'
oldbase = 13
newbase = 15

# find new converted string with new base

# Part I
def hexValue(char):
    if (char >= '0') and (char <= '9'):
        return ord(char) - ord('0')
    else:
        char = char.upper()
        return ord(char) - ord('A') + 10;


def baseEquivalentToNumber(input_string, base):
    power = 0
    total = 0
    for i in range(len(input_string) - 1, -1, -1):
        total = total + (hexValue(input_string[i]) * pow(base, power))
        power = power + 1
    return total

convertedNumber = baseEquivalentToNumber(number, oldbase)
# print(convertedNumber)


# Part II
def chrValue(num):
    if (num >= 0) and (num <= 9):
        return chr(num + ord('0'));
    else:
        return chr(num - 10 + ord('A'));


def baseEquivalentFromNumber(input_number, base):
    newBaseEquivalent = ''
    while input_number > 0:
        rem = input_number % base
        input_number = input_number // base
        newBaseEquivalent = newBaseEquivalent + chrValue(rem)
    return newBaseEquivalent[::-1]


convertedNumber = baseEquivalentFromNumber(convertedNumber, newbase)
print(convertedNumber)