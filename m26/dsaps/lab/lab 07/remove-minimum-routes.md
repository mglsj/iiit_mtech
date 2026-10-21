# Remove Minimum Routes

Bob is the president of country A. The country has `n` cities numbered from 1 to `n`, and city 1 is the capital.

There are `m` bidirectional roads. The `i`-th road connects cities `u_i` and `v_i` and has length `x_i`.

There are also `k` bidirectional train routes. The `i`-th train route connects the capital (city 1) and city `s_i` and has length `y_i`.

Bob wants to save money by closing some of the train routes. However, the length of the shortest path from every city to the capital must **not change**. Both roads and train routes can be used in these paths.

Find the maximum number of train routes that can be closed.

## Input Format

The first line contains three integers `n`, `m`, `k`.

Each of the next `m` lines contains three integers `u_i`, `v_i`, `x_i`, describing a road.

Each of the next `k` lines contains two integers `s_i`, `y_i`, describing a train route.

## Constraints

It is guaranteed that:

- `2 <= n <= 10^5`
- `1 <= m <= 3 * 10^5`
- `1 <= k <= 10^5`
- `1 <= u_i, v_i <= n`, `u_i != v_i`, `1 <= x_i <= 10^9`
- `2 <= s_i <= n`, `1 <= y_i <= 10^9`
- There is **at most one** road between any pair of cities `u` and `v`.
- There is **at most one** train route between the capital 1 and any city `v`. (Hence `k <= n - 1`.)
- Every city can reach the capital.

## Output Format

Output a single integer, the maximum number of train routes that can be closed.

## Sample Input 1

```
5 5 3
1 2 1
2 3 2
1 3 3
3 4 4
1 5 5
3 5
4 5
5 5
```

## Sample Output 1

```
2
```

## Explanation 1

The shortest distances to the capital are 1, 3, 5, 5 for cities 2, 3, 4, 5.

- The train route to city 3 (length 5) is longer than the shortest path (3), so it can be closed.
- The train route to city 4 (length 5) gives the shortest distance (the best road path has length 7), so it must stay.
- The train route to city 5 (length 5) equals the road distance (5), so it can be closed.

## Sample Input 2

```
3 2 2
1 2 3
2 3 3
2 3
3 5
```

## Sample Output 2

```
1
```

## Explanation 2

The road distance to city 2 is 3, which equals the train route length, so that train route can be closed. The road distance to city 3 is 6, but the train route has length 5, so it must stay.
