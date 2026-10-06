# Diameter Of Tree

You are given a tree with `N` nodes, numbered from 1 to `N`, and `N - 1` undirected edges. A tree is a connected graph with no cycles, so there is exactly one path between any two nodes.

The **length** of a path is the number of edges on it.

The **diameter** of the tree is the length of the longest path between any two nodes in the tree.

Find the diameter of the tree.

## Input Format

The first line contains one integer `N` — the number of nodes.

Each of the next `N - 1` lines contains two integers `u` and `v`, meaning there is an undirected edge between node `u` and node `v`.

## Constraints

- `1 <= N <= 10^5`
- `1 <= u, v <= N`
- `u != v`
- The given edges form a tree (the graph is connected and has no cycles).

## Output Format

Print a single integer — the diameter of the tree.

## Sample Input 1

```
5
1 2
1 3
3 4
3 5
```

## Sample Output 1

```
3
```

## Explanation 1

The longest path is 2 → 1 → 3 → 4, which has 3 edges. (The path 2 → 1 → 3 → 5 also has 3 edges.) No path is longer, so the diameter is `3`.

## Sample Input 2

```
1
```

## Sample Output 2

```
0
```

## Explanation 2

The tree has only one node and no edges, so the longest path has 0 edges.

## Sample Input 3

```
8
1 2
2 3
2 4
3 5
5 6
4 7
7 8
```

## Sample Output 3

```
6
```

## Explanation 3

The longest path is 6 → 5 → 3 → 2 → 4 → 7 → 8, which has 6 edges.
