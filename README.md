# coding_interview
Study and implement frequently asked data structure in coding interviews

### Depth First Search (DFS)
  - DFS uses stack data structure (or recursive function) to search the deepest node first.
  
    1. Push start node to the stack and make it **visited**
    2. Find adjacent nodes to the node on the top of the stack
    3. Any adjacent node that is not visited is pushed to the stack
    4. If no adjacent nodes exist or all adjacnet nodes are visited, the node on the top of the stack is popped
    5. Do 2~4 until the stack is empty.
