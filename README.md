# coding_interview
Study and implement frequently asked data structure in coding interviews

### Depth First Search (DFS)
  - DFS uses stack data structure (or recursive function) to search the deepest node first.
  
    1. Push start node to the **stack** and mark it visited
    2. Find adjacent nodes to the node on the top of the stack
    3. Any adjacent node that is not visited is pushed to the stack
    4. If no adjacent nodes exist or all adjacnet nodes are visited, the node on the top of the stack is popped
    5. Do 2~4 until the stack is empty.

### Breath First Search (BFS) 
  - BFS uses queue data structure to search for the most adjcent nodes first

    1. Push start node to the **queue** and mark it visited
    2. Pop the node from the queue
    3. Push unvisited adjcent nodes to the queue and mark them visited
    4. Do 2~3 until the queue is empty
