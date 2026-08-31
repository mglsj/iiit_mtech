# Limited Coin Change

## Problem Description

You are given `n` types of coins. Each type of coin has a denomination value and a limited number of coins available.

You need to determine the number of distinct ways to make a target sum using the given coins.

### Note

- Two ways are considered different if the **number of coins used of any denomination differs**.
- The order of coins does not matter.

## Input

- The first line contains two integers `n` (number of coin types) and `target` (the sum you want to form).
- The next `n` lines each contain two integers:
  - `value[i]` – the denomination of coin type `i`.
  - `count[i]` – the maximum number of coins available of this type.

## Output

Print a single integer: the number of distinct ways to form the target sum.

## Constraints

- `1 ≤ n ≤ 50`
- `1 ≤ target ≤ 5000`
- `1 ≤ value[i] ≤ 100`
- `1 ≤ count[i] ≤ 100`
- The answer fits in a **32-bit signed integer**.

## Sample Input 1

```text
3 5
1 3
2 2
3 1
```

## Sample Output 1

```text
4
```

### Explanation

Ways to make `5`:

- `2 + 3`
- `1 + 1 + 3`
- `1 + 2 + 2`
- `1 + 1 + 1 + 2`

---

## Sample Input 2

```text
2 4
1 3
2 1
```

## Sample Output 2

```text
1
```

### Explanation

Only one way:

`1 + 1 + 2`