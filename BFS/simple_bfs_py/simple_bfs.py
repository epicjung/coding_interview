

def bfs(graph, visited, queue):
    while queue:
        cur_node = queue.pop(0)
        node_number = cur_node[0]
        level = cur_node[1]
        print("Node number: {} at level {}".format(node_number, level))
        for node in graph[node_number]:
            if not visited[node-1]:
                queue.append((node, level+1))
                visited[node-1] = True

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
queue = []

# add first start node
queue.append((1, 1)) # (node number, level)
visited[0] = True # mark visited

bfs(graph, visited, queue)
