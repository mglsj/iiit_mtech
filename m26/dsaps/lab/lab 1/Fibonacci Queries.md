# Fibonacci Queries

## Problem Statement

Fibonacci numbers are one of the most famous sequences occurring in nature.

The Fibonacci sequence is defined by the recurrence relation:

```text
F(0) = 0
F(1) = 1
F(N) = F(N-1) + F(N-2), for N >= 2
```

Fibonacci numbers can grow exceptionally large, far beyond the storage capacity of normal data types.

You are given an integer `Q`, denoting the number of queries. Each query contains an integer `N`.

For every query, return the **N-th Fibonacci number**.

Since `N` can be large, return each answer **modulo `1000000007` (`10^9 + 7`)**.

## Input Format

- The first line contains an integer `Q`, denoting the number of queries.
- The next `Q` lines contain one integer per query: `N₁, N₂, ..., NQ`.

## Output Format

Print `Q` lines.

Each line should contain the Fibonacci number corresponding to the respective query, modulo `10^9 + 7`.

## Constraints

- `1 ≤ Q ≤ 10^4`
- `1 ≤ N[i] ≤ 10^6`

## Sample Input

```text
5
4
2
3
100
14769
```

## Sample Output

```text
3
1
2
687995182
13755455
```