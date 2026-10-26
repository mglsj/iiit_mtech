# Pair XOR Sum

You are given an array `a` of `n` non-negative integers.

Find the sum of `a_i ⊕ a_j` over all pairs `(i, j)` with `1 <= i < j <= n`.

Here `⊕` means the bitwise XOR operation.

## Input Format

- The first line has one integer `n`, the size of the array.
- The second line has `n` space-separated integers `a_1, a_2, ..., a_n`.

## Constraints

- `1 <= n <= 10^5`
- `0 <= a_i <= 10^9`

## Output Format

Print one integer, the sum of `a_i ⊕ a_j` over all pairs `i < j`.

## Sample Input 1

```
3
1 2 3
```

## Sample Output 1

```
6
```

## Explanation 1

The pairs are:

- `1 ⊕ 2 = 3`
- `1 ⊕ 3 = 2`
- `2 ⊕ 3 = 1`

The sum is 3 + 2 + 1 = 6.

## Sample Input 2

```
4
1 2 4 8
```

## Sample Output 2

```
45
```

## Explanation 2

The pairs are:

- `1 ⊕ 2 = 3`
- `1 ⊕ 4 = 5`
- `1 ⊕ 8 = 9`
- `2 ⊕ 4 = 6`
- `2 ⊕ 8 = 10`
- `4 ⊕ 8 = 12`

The sum is 3 + 5 + 9 + 6 + 10 + 12 = 45.
