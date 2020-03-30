input_string = '3/2^3'

#make a function named isnumeric(string)
def isnumeric(in_string):
    str_x = str(in_string)
    counter = 0
    for x in str_x:
        if x in ['/', '^']:
            counter = counter + 1
    if counter > 1:
        print('False NaN')


isnumeric(input_string)


input_string2 = '3^1.3'

value = eval(input_string2)
value = round(value,4)
print("True {0}".format(value))
ç