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

  - Applications:

    - Shortest distance from start to end 

### Sorting
  - **Selection sort** - O(N^2)
    
    1. Find smallest element from the unmanaged elements
    2. Swap the found element with the front most element in the unmanaged elements
    3. Until the unmanaged element is left with one

  - **Insertion sort**
    - worst: O(N^2)
    - best: O(N)
   
    ![alt text](https://github.com/epicjung/coding_interview/blob/main/images/insertion_sort.png?raw=true)
    
    1. Assume the first element '7' is already sorted, the second data '5' is either inserted into 7's left or right
    2. Do above step until the pointer reaches the end of the list
  
  - **Quick sort**
    - Best: O(NlogN)
    - Worst: O(N^2) - already sorted list
    - Set a pivot data and swapping the elements that are bigger and smaller than the pivot data
    - When comparing the two elements, two pointers from the end (finding smaller element) and start (finding larger element) approach to the center.
    - Usually, the pitvot data is the first data of the list
       
      ![alt text](https://github.com/epicjung/coding_interview/blob/main/images/quick_sort.png?raw=true)

    - If two pointers intersect, the smaller data will be swapped with the pivot data.
    - Now, divide is completed
      
      ![alt text](https://github.com/epicjung/coding_interview/blob/main/images/quick_sort_divide.png?raw=true)

    - Start with a new pivot in each of the divided list

  - **counting sort** 



  ![alt text](https://github.com/epicjung/coding_interview/blob/main/images/sort_comparison.png?raw=true)
