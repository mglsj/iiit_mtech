# Knapsack Problem

There are **N** items, numbered `1, 2, …, N`.

For each item `i` (`1 ≤ i ≤ N`):

- It has a **weight** `w_i`.
- It has a **value** `v_i`.

Taro wants to choose some of the items and carry them in a knapsack.

**Each item can only be taken at most once.**

## Knapsack Capacity

The knapsack has capacity **W**, meaning:

> The **sum of weights** of chosen items must be **at most W**.

## Goal

Find the **maximum possible sum of values** of items Taro takes home.

## Constraints

- `1 ≤ N ≤ 1000`
- `1 ≤ W ≤ 10^5`
- `1 ≤ w_i, v_i ≤ 1000`
- All input values are integers.

## Input Format

```text
N W
w1 w2 w3 .. wN
v1 v2 v3 .. vN
```

## Output Format

Print the **maximum possible sum of values** of items chosen.

## Sample Input 1

```text
3 8
3 4 5
30 50 60
```

## Sample Output 1

```text
90
```

### Explanation

Choose items `1` and `3`.

- Weight = `3 + 5 = 8`
- Value = `30 + 60 = 90`

---

## Sample Input 2

```text
6 15
6 5 6 6 3 7
5 6 4 6 5 2
```

## Sample Output 2

```text
17
```

### Explanation

Choose items `2`, `4` and `5`.

- Weight = `5 + 6 + 3 = 14`
- Value = `6 + 6 + 5 = 17`