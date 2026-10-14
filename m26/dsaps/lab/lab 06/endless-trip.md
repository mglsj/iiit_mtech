# Endless Trip

Bob lives in country G with `N` cities, labeled city 1, city 2, …, city `N`. The cities are connected by `M` unidirectional (one-way) roads. The `i`-th road (`1 <= i <= M`) goes from city `X_i` to city `Y_i`.

Bob loves travelling and wants to keep moving without ever hitting a dead end. Help Bob find the number of cities such that, starting from that city, he can follow a path that **never ends**.

Note that in country G there may be two roads in opposite directions between the same pair of cities. Additionally, G may not be connected.

## Input Format

The first line contains two space-separated integers `N` and `M`, the number of cities and the number of roads, respectively.

Each of the next `M` lines contains two space-separated integers `X_i` and `Y_i`, denoting the starting and ending city of the `i`-th road.

## Constraints

- `1 <= N <= 2 * 10^5`
- `0 <= M <= min(N(N - 1), 2 * 10^5)`
- `1 <= X_i, Y_i <= N`

## Output Format

Print a single integer: the number of cities from which Bob can travel indefinitely.

## Sample Input 1

```
5 5
1 2
2 3
3 4
4 2
4 5
```

## Sample Output 1

```
4
```

## Explanation 1

Starting at city 2, Bob can travel indefinitely: 2 → 3 → 4 → 2 → 3 → ⋯. The same holds for cities 3 and 4. From city 1, he can first go to city 2 and then continue forever. From city 5, he cannot move at all.

Thus four cities (cities 1, 2, 3, 4) satisfy the condition, so `4` is printed.

## Sample Input 2

```
3 2
1 2
2 1
```

## Sample Output 2

```
2
```

## Explanation 2

Cities 1 and 2 form a cycle, and city 3 has no roads, so the answer is `2`.
