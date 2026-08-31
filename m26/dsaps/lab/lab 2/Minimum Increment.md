# Minimum Increment

## Problem Statement

You are given an integer array `nums`.

In one move, you can pick an index `i` where:

`0 ≤ i < nums.length`

and increment `nums[i]` by `1`.

Return the **minimum number of moves** to make every value in `nums` unique.

## Constraints

The first line of input contains a single integer `n`, the length of the array `nums`.

The second line contains `n` space-separated integers, the elements of `nums`.

- `1 ≤ n ≤ 10^5`
- `0 ≤ nums[i] ≤ 10^5`

## Output

Output a single integer, the minimum number of moves required to make every value in `nums` unique.

## Sample Input 1

```text
3
1 2 2
```

## Sample Output 1

```text
1
```

### Explanation for Sample 1

After 1 move, the array could be:

```text
[1, 2, 3]
```

---

## Sample Input 2

```text
6
3 2 1 2 1 7
```

## Sample Output 2

```text
6
```

### Explanation for Sample 2

After 6 moves, the array could be:

```text
[3, 4, 1, 2, 5, 7]
```

It can be shown that it is impossible for the array to have all unique values with 5 or fewer moves.