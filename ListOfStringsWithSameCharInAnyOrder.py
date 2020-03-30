
def NestedListUniqueValue(vInputList):

    vInputList = sorted(vInputList)
    parent_list = []

    for word1 in vInputList:
        child_list = list()
        child_list.append(word1)

        for word2 in vInputList[1:]:
            if sorted(word1) == sorted(word2):
                child_list.append(word2)
                vInputList.remove(word2)

        parent_list.append(list(set(child_list)))

    return print(parent_list)

inputList = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

import time
start_time = time.time()

# my code here

NestedListUniqueValue(inputList)

# Output: [['eat', 'ate', 'tea'], ['bat'], ['tan', 'nat']]


print ("\nTime Elapsed: {:.2f}s".format(time.time() - start_time))
