#  N x M matrix with 0's and 1's
#  An element is connected if it is 0 and its adjcents (up, down, left, right) have 0 as well
#  How many connected cluster can be made?

#  [ 0 0 1 1 0 ]
#  [ 0 0 0 1 1 ]
#  [ 1 1 1 1 1 ]
#  [ 0 0 0 0 0 ]
#  Above NxM matrix has 3 clusters (icecreams)

# 1 <= N, M <= 10000
# This problem can be solved either using DFS or BFS

def get_adjacent(matrix, coord, adjacents, visited):
    steps = [(0,1), (1, 0), (-1, 0), (0, -1)]
    for ii, ij in steps:
        new_i = coord[0] + ii
        new_j = coord[1] + ij
        if new_i < 0 or new_j < 0 or new_i >= len(matrix) or new_j >= len(matrix[0]):
            continue
        if matrix[new_i][new_j] == '0':
            key = coord_to_key((new_i, new_j))
            if not_visited(key, visited):
                adjacents.append((new_i, new_j))

def not_visited(key, visited):
    return key not in visited or not visited[key] 

def coord_to_key(coord):
    return "{}{}".format(coord[0],coord[1])

def bfs(matrix, coord, queue, visited, answer, level):
    key = coord_to_key(coord)
    queue.append((coord, level))
    visited[key] = True
    while queue:
        cur_node = queue.pop(0)
        cur_coord = cur_node[0]
        cur_level = cur_node[1]
        cur_key = coord_to_key(cur_coord)
        answer.append((cur_key, cur_level))
        adjacents = []
        get_adjacent(matrix, cur_coord, adjacents, visited)
        for adj_coord in adjacents:
            adj_key = coord_to_key(adj_coord)
            if not_visited(adj_key, visited):
                visited[adj_key] = True
                queue.append((adj_coord, cur_level+1))

def bfs_method(matrix, N, M):
    visited = {}
    queue = []
    start_node_cnt = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '0':
                key = coord_to_key((i, j))
                if not_visited(key, visited): # start node
                    start_node_cnt += 1
                    level = 0
                    answer = []
                    bfs(matrix, (i, j), queue, visited, answer, level)
                    print("Icecream #{}: {}".format(start_node_cnt, answer))
    
    print("Total icecream: {}".format(start_node_cnt))

def dfs(matrix, coord, visited, answer, level):
    key = coord_to_key(coord)
    if not_visited(key, visited):
        visited[key] = True
        adjacents = []
        answer.append((key, level))
        get_adjacent(matrix,(coord[0], coord[1]), adjacents, visited)
        for adj_coord in adjacents:
            dfs(matrix, adj_coord, visited, answer, level+1)

def dfs_method(matrix, N, M):
    visited = {}
    start_node_cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '0':
                start_key = coord_to_key((i, j))
                if not_visited(start_key, visited): # start node
                    answer = []
                    start_node_cnt += 1
                    level = 0
                    dfs(matrix, (i, j), visited, answer, level)
                    print("Icecream #{}: {}".format(start_node_cnt, answer))
    
    print("Total icecream: {}".format(start_node_cnt))
    

sample_input = "4 5\n00110\n00011\n11111\n00000"
input_array = sample_input.split('\n')
N = int(input_array[0].split(' ')[0])
M = int(input_array[0].split(' ')[1])
matrix = input_array[1:]
bfs_method(matrix, N, M)

sample_input = "3 3\n001\n010\n101"
input_array = sample_input.split('\n')
N = int(input_array[0].split(' ')[0])
M = int(input_array[0].split(' ')[1])
matrix = input_array[1:]
bfs_method(matrix, N, M)