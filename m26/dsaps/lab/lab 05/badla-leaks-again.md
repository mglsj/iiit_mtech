# Badla Leaks Again

Badla is a TA for some other course. He has nothing to do with DSAPS, which has never stopped him from "helping" DSAPS students. Tonight, the night before the lab, he has somehow got hold of one of the lab questions, and he wants every DSAPS student to see it before tomorrow.

Posting it on the batch group is out of the question, since the DSAPS TAs are in that group and are watching. So Badla falls back on the most reliable communication system on campus: hostel gossip. He will text the question to a few students, and any student who receives it immediately forwards it to every friend they directly talk to, who forward it to their friends, and so on. Badla is lazy, so he wants to send as few texts as possible, but he still wants every student to have the question before the lab starts.

You are given an undirected graph representing the friendships on campus (`1` to `n`), where each node corresponds to a student, and each edge represents two students who directly talk to each other.

A **cluster** is defined as a group of nodes that are connected directly or indirectly. Your task is to find how many such clusters (connected components) exist in the network, so Badla knows the minimum number of texts he needs to send.

## Input Format

The first line contains `n` (number of nodes) and `e` (number of edges).

The next `e` lines contain `a` and `b`, denoting an edge between `a` and `b`.

## Constraints

- `1 <= n <= 500`

## Output Format

Output an integer representing the number of clusters in the network.

## Sample Input 1

```
3 1
1 3
```

## Sample Output 1

```
2
```

## Explanation 1

The graph clearly has 2 components, `[1, 3]` and `[2]`. As 1 and 3 have a path between them, they belong to a single component. 2 has no path to 1 or 3, hence it belongs to another component.
