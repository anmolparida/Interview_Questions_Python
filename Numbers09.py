
for A in range(1,10):
    for B in range(1, 10):
        for C in range(1, 10):
            for D in range(1, 10):
                for E in range(1, 10):
                    for F in range(1, 10):
                        for G in range(1, 10):
                            for H in range(1, 10):
                                for I in range(1, 10):

                                    line1 = [A,B]
                                    line2 = C
                                    line3 = [D,E]
                                    line4 = [F,G]
                                    line5 = [H,I]

                                    validation_list = []
                                    validation_list.append(line1[0])
                                    validation_list.append(line1[1])
                                    validation_list.append(line2)
                                    validation_list.append(line3[0])
                                    validation_list.append(line3[1])
                                    validation_list.append(line4[0])
                                    validation_list.append(line4[1])
                                    validation_list.append(line5[0])
                                    validation_list.append(line5[1])



                                    validation_set = set()
                                    validation_set.add(line1[0])
                                    validation_set.add(line1[1])
                                    validation_set.add(line2)
                                    validation_set.add(line3[0])
                                    validation_set.add(line3[1])
                                    validation_set.add(line4[0])
                                    validation_set.add(line4[1])
                                    validation_set.add(line5[0])
                                    validation_set.add(line5[1])

                                    # if validation_list == [1,7,4,6,8,2,5,9,3]:
                                        print(validation_list)
                                        if validation_set == {1,2,3,4,5,6,7,8,9}:
                                            if (int(str(line1[0]) + str(line1[1])) * line2) + (int(str(line3[0]) + str(line3[1]))) ==  int(str(line4[0]) + str(line4[1])):
                                                print('Line 1 : ' + str(line1))
                                                print('Line 2 : ' + str(line2))
                                                print('Line 3 : ' + str(line3))
                                                print('Line 4 : ' + str(line3))
                                                print('Line 5 : ' + str(line5))
                                                print('------')








#         print('A : ' + str(line1[0]))
#         print('B : ' + str(line1[1]))
#         print('C : ' + str(line2))
#         print('D : ' + str(line3[0]))
#         print('E : ' + str(line3[1]))
#         print('F : ' + str(line4[0]))
#         print('G : ' + str(line4[1]))
#         print('H : ' + str(line5[0]))
#         print('I : ' + str(line5[1]))

