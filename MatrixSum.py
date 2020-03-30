# # Creating the Matrix from input
#
# numberOfRows = int(input('Enter the numberOfRows: '))
# numberOfCols = int(input('Enter the numberOfCols: '))
#
# matrix = []
# for c in range(numberOfCols):
#     row = []
#     print('<< Enter the values in row wise >> ')
#     for r in range(numberOfRows):
#         rowValue = int(input('Enter the value: '))
#         row.append(rowValue)
#     matrix.append(row)
#
# print (matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # Printing in Matrix Format

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for rows in matrix:
    for cols in rows:
        print (cols)


print (matrix)



