
import copy

# Question:
# Island: 1's that are not connected to the border of 1's in the matrix  

def is_border(matrix, i, j):
    if i == 0 or j == 0 or i == len(matrix) -1 or j == len(matrix[0]) - 1:
        return True
    return False

def outside_matrix(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return True
    return False

def adjacent_to_one(matrix, i, j, adjacent_coords): # recursion
    steps = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    
    for ii, ij in steps:
        new_i = i + ii
        new_j = j + ij
        if outside_matrix(matrix, new_i, new_j):
            continue
        if matrix[new_i][new_j] == 1:
            if (new_i, new_j) not in adjacent_coords:
                adjacent_coords.append((new_i, new_j))
                adjacent_to_one(matrix, new_i, new_j, adjacent_coords)
    
def removeIslands(matrix):
    connected = []
    output = copy.deepcopy(matrix)
    
    # finish this in single loop
    # O(n*m)
    # In recursion, you are doing constant operation for each element so still O(n*m)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            adjacent_coords = []
            if is_border(matrix, i, j) and matrix[i][j] == 1:
                adjacent_to_one(matrix, i, j, adjacent_coords)
                for coord in adjacent_coords:
                    connected.append(coord)
                    output[coord[0]][coord[1]] = 1
            elif not is_border(matrix, i, j) and matrix[i][j] == 1:
                adjacent_to_one(matrix, i, j, adjacent_coords)
                if len(adjacent_coords) == 0:
                    output[i][j] = 0
                else:
                    for coord in adjacent_coords:
                        if coord not in connected:
                            output[i][j] = 0

    return output
    

matrix1 = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

sample_output1 = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

matrix2 = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

sample_output2 = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]   
]


if removeIslands(matrix1) == sample_output1:
   print("1: Success!")

if removeIslands(matrix2) == sample_output2:
    print("2: Success!")
