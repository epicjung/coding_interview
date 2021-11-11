# Tip: Don't need visited as we can make the graph element 1 to inidicate it's visited
# 1. loop through matrix
# 2. Finds 0 then bfs search from that 0 and mark visited element to 1
# 3. When queue is empty, all the visited node will be skipped in a loop because they are all 1 

sample_input = "4 5\n00110\n00011\n11111\n00000"
input_array = sample_input.split('\n')
n, m = map(int, input_array[0].split())

graph = []
for i in range(n):
    graph.append(list(map(int, input_array[1+i])))

def bfs(x, y, answer):
    queue.append((x, y, 0))
    answer.append((x, y, 0))
    graph[x][y] = 1
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        popped = queue.pop(0)
        cur_x = popped[0]
        cur_y = popped[1]
        cur_level = popped[2]
        for ix, iy in steps:
            adj_x = cur_x + ix
            adj_y = cur_y + iy
            if adj_x <= -1 or adj_x >= n or adj_y <= -1 or adj_y >= m:
                continue
            if graph[adj_x][adj_y] == 0:
                graph[adj_x][adj_y] = 1
                answer.append((adj_x, adj_y, cur_level+1))
                queue.append((adj_x, adj_y, cur_level+1))
        
queue = []
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer = []
            result += 1
            bfs(i, j, answer)
            print("Icecream #{}: {}".format(result, answer))
print(result)