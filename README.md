# Assignment-cgt

The task involves creating a dynamic and engaging program that takes a random graphic sequence as input and generates a corresponding graph using the Havel-Hakimi algorithm. 
Once the graph is constructed, the program performs several fascinating operations on it:

1. Graph Construction & Eulerian Check: The program first builds the graph and then checks if it's an Eulerian graph.
   i.e., whether it contains an Eulerian path or circuit. 

2. Shortest Path Calculation: Random weights are assigned to the graph’s edges.
   The user picks a starting vertex, and the program calculates the shortest path to all other vertices using Dijkstra’s algorithm.

3. Minimum Spanning Tree: Next, the program finds the minimum spanning tree (MST) using  Kruskal’s algorithm.
   The MST connects all vertices with the minimum total edge weight.

4. Fundamental Cutsets & Circuits: With the MST as a base, the program identifies fundamental cutsets and fundamental circuits .

5. Connectivity Analysis: Finally, the program analyzes the graph’s edge connectivity and vertex connectivity.

6. It also determines its K-connectedness.
