
def dfs(graph, node_number, visited, level):
    visited[node_number-1] = True
    level += 1
    print("Visited: {} at level: {}".format(node_number, level))
    for node in graph[node_number]:
        if not visited[node-1]:
            dfs(graph, node, visited, level)

graph = [
    [], # Node 0's adjacent nodes
    [2, 3, 8], # Node 1's adjcent nodes
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9 # Node 0 ~ 8
level = 0
dfs(graph, 1, visited, level)
