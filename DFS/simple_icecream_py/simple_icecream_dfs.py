# Tip: Don't need visited as we can make the graph element 1 to inidicate it's visited
# 1. loop through matrix
# 2. Finds 0 then dfs search from that 0 and mark visited element to 1
# 3. After getting out of recursion, all the visited node will be skipped in a loop because they are all 1 

sample_input = "4 5\n00110\n00011\n11111\n00000"
input_array = sample_input.split('\n')
n, m = map(int, input_array[0].split())

graph = []
for i in range(n):
    graph.append(list(map(int, input_array[1+i])))
    
def dfs(x, y, answer, level):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        answer.append(((x,y),level))
        level += 1
        dfs(x-1, y, answer, level)
        dfs(x, y-1, answer, level)
        dfs(x+1, y, answer, level)
        dfs(x, y+1, answer, level)
        return True
    return False

result = 0
answer = []
for i in range(n):
    for j in range(m):
        if dfs(i, j, answer, 0):
            result += 1
            print("Icecream #{}: {}".format(result, answer))
            answer = []
