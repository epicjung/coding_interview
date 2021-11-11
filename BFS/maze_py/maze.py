# Stuck in N x M matrix
# 0: monster, 1: no monster
# Start at (1, 1), exit is at (N, M)
# minimum number of step (up down left right) to get to the exit 

# 4 <= N, M <= 200

sample_input = "5 6\n101010\n111111\n000001\n111111\n111111"
input_array = sample_input.split('\n')
n, m = map(int, input_array[0].split())

graph = []
for i in range(n):
    graph.append(list(map(int, input_array[1+i])))

queue = []
start = (0, 0)
queue.append((start, 1))
graph[start[0]][start[1]] = 0
steps = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while queue:
    popped = queue.pop(0)
    cur_coord = popped[0]
    cur_level = popped[1]

    if cur_coord[0] == n-1 and cur_coord[1] == m-1:
        print(cur_level)
        break

    for ix, iy in steps:
        adj_x = cur_coord[0] + ix
        adj_y = cur_coord[1] + iy
        if adj_x <= -1 or adj_x >= n or adj_y <= -1 or adj_y >= m:
            continue
        if graph[adj_x][adj_y] == 1:
            graph[adj_x][adj_y] = 0
            queue.append(((adj_x, adj_y), cur_level+1))
