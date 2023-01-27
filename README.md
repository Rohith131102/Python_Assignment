# Python-Assignment

As the board entries need to be traversed, I came up with two ways to the problem. The code for both of these techniques is added as.py files.

- Breadth First Search
- Depth First Search

## 1. Breadth First Search
A data structure is searched for an element using the BFS algorithm, often known as breadth-first search. Before moving on to entries at the following depth level, it starts at a specific element and explores all nodes at the current depth level.

#### Implementation of BFS

In order to determine which "O" entries are connected to it because one of its sides is already filled by "O," we have crossed the board's borders and applied BFS to all of those entries. In contrast to previous entries, which were changed to "X" because they cannot be captured, we then label all of these types of entries as "$" and transform them to "O."

We used queues in the BFS construction process. Every time we eliminated an entry from the queue, we went through the surrounding elements and added them to the queue.

## 2. Depth First Search

An algorithm for searching in data structures is called depth-first search. The method starts at a random node and travels as far as it can along each branch before turning around.

#### Implementation of DFS

In order to determine which "O" entries are connected to it and therefore cannot be captured by "X" because one of its sides is occupied by "O," we traversed the board's borders and performed DFS to all of the "O" entries in the borders. We then marked all of these types of entries to "$" and transformed them to "O," whereas other entries were made to "X" because they could be captured.
