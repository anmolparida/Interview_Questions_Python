input_list = [5, 4, 6, 3, 8, 4, 2]
# input_list = [12, 18, 11, 24, 55]

local_maxima = []
local_minima = []


def localMaxima(vList):

    if input_list[0] > input_list[1]:
        local_maxima.append(input_list[0])

    for x in range(1,len(input_list)-1):

        if (input_list[x] > input_list[x-1]) and (input_list[x] > input_list[x+1]):
            local_maxima.append(input_list[x])

    if input_list[-1] > input_list[-2]:
        local_maxima.append(input_list[-1])

    print(local_maxima)


def localMinima(vList):

    if input_list[0] < input_list[1]:
        local_minima.append(input_list[0])

    for x in range(1, len(input_list) - 1):

        if (input_list[x] < input_list[x - 1]) and (input_list[x] < input_list[x + 1]):
            local_minima.append(input_list[x])

    if input_list[-1] < input_list[-2]:
        local_minima.append(input_list[-1])

    print(local_minima)



localMaxima(input_list)

localMinima(input_list)


