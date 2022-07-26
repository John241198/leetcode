matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#initial solution

"""
In a first for loop we transport the 3*3 matrix using swapping matrix element one by one in loop
and second for loop reverse the transport matrix resulted matrix output is obtained
"""

for row in range(len(matrix)):
    for col in range(0, row + 1):
        if row != col:
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
for row in range(len(matrix)):
    matrix[row] = matrix[row][::-1]
print(matrix)