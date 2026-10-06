# Minimum No Of Edges

You are given an undirected graph with `N` nodes, numbered from 1 to `N`, and `M` edges. You are also given a starting node `S`.

You start at node `S`. In one move, you can go from your current node to any node that is connected to it by an edge.

For every node in the graph, find the **minimum number of moves** needed to reach it from node `S`. If a node cannot be reached from `S`, print `-1` for that node.

## Input Format

The first line contains two integers `N` and `M` — the number of nodes and the number of edges.

Each of the next `M` lines contains two integers `u` and `v`, meaning there is an undirected edge between node `u` and node `v`.

The last line contains a single integer `S` — the starting node.

## Constraints

- `1 <= N <= 10^5`
- `0 <= M <= 2 * 10^5`
- `1 <= u, v <= N`
- `u != v`
- There is at most one edge between any pair of nodes.
- `1 <= S <= N`

## Output Format

Print `N` space-separated integers. The `i`-th integer should be the minimum number of moves needed to go from node `S` to node `i`, or `-1` if node `i` cannot be reached from `S`.

## Sample Input 1

```
6 6
1 2
2 3
3 4
4 5
5 6
1 6
1
```

## Sample Output 1

```
0 1 2 3 2 1
```

## Explanation 1

The graph is a cycle 1 – 2 – 3 – 4 – 5 – 6 – 1. Node 1 is the start, so it needs 0 moves. Nodes 2 and 6 are direct neighbours of node 1, so they need 1 move each. Node 3 is reached by 1 → 2 → 3 and node 5 by 1 → 6 → 5, so each needs 2 moves. Node 4 can be reached either way around the cycle in 3 moves. Note that for node 5, the path 1 → 2 → 3 → 4 → 5 takes 4 moves, but going the other way around the cycle is shorter, so its answer is 2.

## Sample Input 2

```
5 4
1 2
1 3
3 4
3 5
4
```

## Sample Output 2

```
2 3 1 0 2
```

## Explanation 2

The start is node 4, so its answer is 0. Node 3 is its only neighbour (1 move). From node 3 we reach nodes 1 and 5 (2 moves), and from node 1 we reach node 2 (3 moves).

## Sample Input 3

```
7 7
1 2
2 3
3 7
1 4
4 7
5 6
2 4
2
```

## Sample Output 3

```
1 0 1 1 -1 -1 2
```

## Explanation 3

Nodes 1, 3 and 4 are direct neighbours of node 2, so they need 1 move each. Node 7 can be reached by 2 → 3 → 7 or 2 → 4 → 7, which takes 2 moves. Since there is no edge between node 2 and node 7, it cannot be done in 1 move. Nodes 5 and 6 are only connected to each other, so they cannot be reached from node 2, and their answers are `-1`.
