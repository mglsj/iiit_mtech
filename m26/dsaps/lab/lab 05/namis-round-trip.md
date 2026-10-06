# Nami's Round Trip

The Straw Hat Pirates are sailing the Grand Line. Nami, the crew's navigator, has a sea chart with `N` islands and `M` sea routes. Every sea route connects two islands, and the ship can sail along it in both directions.

On the Grand Line, normal compasses do not work, so ships navigate with a Log Pose. The Log Pose can only guide the ship along the sea routes on Nami's chart. This means the crew can sail directly from one island to another only if there is a sea route between them. If two islands are not connected by a sea route, the crew cannot sail straight between them.

Luffy wants to go on a round trip: start at **any** island, sail along the sea routes, and come back to the starting island. No sea route is reused in a round trip. Help Nami find out if such a round trip exists.

Islands are numbered from 1 to `N`. A **round trip** is a sequence of islands

`x1 -> x2 -> ... -> xk -> x1`

such that:

1. `k >= 3`, and the islands `x1, x2, ..., xk` are all different.
2. There is a sea route between every pair of consecutive islands in the sequence, including the last step from `xk` back to `x1` (because of the Log Pose, the crew can only sail along sea routes).
3. No sea route is used more than once.

Print `YES` if at least one round trip exists, otherwise print `NO`.

Note: sailing from an island to its neighbour and straight back along the same route (for example 1 → 2 → 1) is not a round trip, because it uses the same sea route twice.

In graph terms: the islands are the nodes, the sea routes are the edges of an undirected graph, and a round trip is a cycle. You need to check whether the graph contains a cycle.

## Input Format

The first line contains two integers `N` and `M` — the number of islands and the number of sea routes.

Each of the next `M` lines contains two integers `u` and `v`, meaning there is a sea route between island `u` and island `v`. The crew can sail this route from `u` to `v` and from `v` to `u`, so the order of the two numbers does not matter: `u v` and `v u` describe the same sea route.

## Constraints

- `1 <= N <= 10^5`
- `0 <= M <= 2 * 10^5`
- `1 <= u, v <= N`
- `u != v` (no sea route starts and ends at the same island)
- There is at most one sea route between any pair of islands.

## Output Format

Print a single line containing `YES` if a round trip exists, or `NO` if it does not.

## Sample Input 1

```
5 5
1 2
2 3
3 1
3 4
4 5
```

## Sample Output 1

```
YES
```

## Explanation 1

The round trip 1 → 2 → 3 → 1 exists: it visits 3 different islands, uses 3 different sea routes (1-2, 2-3, 3-1), and ends at island 1 where it started. So the answer is `YES`.

## Sample Input 2

```
4 3
1 2
2 3
3 4
```

## Sample Output 2

```
NO
```

## Explanation 2

The islands form a straight line: 1 - 2 - 3 - 4.

Suppose the crew starts at island 1 and sails 1 → 2 → 3 → 4. At island 4, the only route is 3 - 4, which has already been used, so the crew cannot get back to island 1. (Sailing back 4 → 3 → 2 → 1 would reuse sea routes, which is not allowed.)

Starting from any other island fails in the same way, so there is no round trip, and the answer is `NO`.

## Sample Input 3

```
6 4
1 2
1 3
1 4
5 6
```

## Sample Output 3

```
NO
```

## Explanation 3

No round trip exists, so the answer is `NO`.

## Sample Input 4

```
7 5
1 2
3 4
4 5
5 6
6 4
```

## Sample Output 4

```
YES
```

## Explanation 4

The round trip 4 → 5 → 6 → 4 exists, so the answer is `YES`.
