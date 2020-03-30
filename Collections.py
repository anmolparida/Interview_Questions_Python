# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


vList = ["apple", "banana", "cherry"]
vList[0] = 'Mango'
print(vList)
print(vList[-1][-4:])


fruit = 'banana'
price = 20
if fruit in vList:
    print("{} in this list, Price per Dozen: {}".format(fruit, price))
else:
    print(fruit + ' NOT in this list, Price per Dozen: ' + str(price))


