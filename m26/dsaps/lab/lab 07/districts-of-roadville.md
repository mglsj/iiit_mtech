# Districts of Roadville

Roadville has `N` towns, numbered from 1 to `N`, connected by `M` one-way roads. A road from town `u` to town `v` can only be used to drive from `u` to `v`, never from `v` to `u`.

The mayor wants to split Roadville into districts, so that people living in the same district can always visit each other.

We say there is a **round trip** between two towns `A` and `B` if you can drive from `A` to `B` and then drive from `B` back to `A`. On the way you may pass through any other towns.

For example, with the roads 1 → 2, 2 → 3 and 3 → 1, there is a round trip between towns 1 and 3: drive 1 → 2 → 3, then 3 → 1.

The rule for the districts is:

- If there is a round trip between two towns, they must be in the same district.
- If there is no round trip between two towns, they must be in different districts.

So a town with no round trip to any other town forms a district on its own.

How many districts will Roadville have?

## Input Format

The first line contains two integers `N` and `M` — the number of towns and the number of roads.

Each of the next `M` lines contains two integers `u` and `v`, meaning there is a one-way road from town `u` to town `v`.

## Constraints

- `1 <= N <= 10^5`
- `0 <= M <= 2 * 10^5`
- `1 <= u, v <= N`
- `u != v`
- No road from `u` to `v` appears more than once (but a road from `u` to `v` and a road from `v` to `u` can both exist).

## Output Format

Print a single integer — the number of districts.

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
3
```

## Explanation 1

You can drive 1 → 2 → 3 → 1, so there is a round trip between any two of the towns 1, 2 and 3. They form one district.

From town 3 you can drive to town 4, but there is no way to drive from 4 back to 3, so there is no round trip between them. Town 4 has no round trip with any town, so it is a district on its own. The same is true for town 5.

The districts are {1, 2, 3}, {4} and {5}, so the answer is `3`.

## Sample Input 2

```
4 3
1 2
2 1
3 4
```

## Sample Output 2

```
3
```

## Explanation 2

Towns 1 and 2 have roads in both directions, so there is a round trip between them: they form one district. There is a road from 3 to 4 but none back, so there is no round trip between 3 and 4, and they are in different districts.

The districts are {1, 2}, {3} and {4}, so the answer is `3`.

## Sample Input 3

```
3 0
```

## Sample Output 3

```
3
```

## Explanation 3

There are no roads at all, so there are no round trips, and every town is a district on its own.
