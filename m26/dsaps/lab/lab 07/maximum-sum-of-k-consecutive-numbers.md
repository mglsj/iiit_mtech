# Maximum Sum of K Consecutive Numbers

You are given an array `A` of `N` integers and an integer `K`.

Find the maximum sum of `K` consecutive elements of the array.

## Input Format

The first line contains two integers `N` and `K`.

The second line contains `N` integers `A[1], A[2], ..., A[N]`.

## Constraints

- `1 <= K <= N <= 5 * 10^5`
- `-10^9 <= A[i] <= 10^9`

## Output Format

Print a single integer — the maximum sum of `K` consecutive elements.

## Sample Input 1

```
6 3
2 -1 4 1 -3 5
```

## Sample Output 1

```
5
```

## Explanation 1

The groups of 3 consecutive elements are:

| Elements | Sum |
|---|---|
| 2, -1, 4 | 5 |
| -1, 4, 1 | 4 |
| 4, 1, -3 | 2 |
| 1, -3, 5 | 3 |

The largest sum is 5.

## Sample Input 2

```
4 2
-5 -2 -3 -7
```

## Sample Output 2

```
-5
```

## Explanation 2

The groups of 2 consecutive elements have sums -7, -5 and -10. The largest is -5. Note that the answer can be negative.

## Sample Input 3

```
5 2
1 2 3 4 5
```

## Sample Output 3

```
9
```

## Explanation 3

The best group is the last one, 4 and 5, with sum 9.
