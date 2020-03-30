def IndicesAddingToSum(inputList, total):
    parent_list = []

    for i in range(0,len(inputList)):
        child_list = []

        for j in range(0,len(inputList)):
            if inputList[i]+inputList[j] == total:
                child_list.append(i)
                child_list.append(j)

                parent_list.append(child_list) # >> [[0, 1], [1, 0], [3, 4], [4, 3]]

                # child_list.reverse() # or use child_list[::-1]
                if child_list[::-1] in parent_list:
                    parent_list.remove(child_list) # >> [[0, 1], [3, 4]]

    print(parent_list)

ListOfNum = [2,7,11,15,-6]
vSum = 9

IndicesAddingToSum(ListOfNum, vSum)

