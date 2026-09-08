# FiboFast

## Problem Statement

Long ago, in the ancient kingdom of Numaria, there lived a wise mathematician who discovered a mystical sequence of numbers. The first two numbers were simple — `0` and `1` — but each number after that was the sum of the previous two.

One day, the King summoned you, the royal programmer, and gave you a monumental task:

> "Tell me the N-th number in this sacred sequence."

But there was a catch — `N` could be unimaginably large, up to `10^18`! The King warned that using slow methods would take centuries, and you had only moments to deliver the answer.

You must compute the **N-th Fibonacci number quickly** and return it **modulo `1e9 + 7`** to prevent the number from becoming too large.

## Fibonacci Sequence

The Fibonacci sequence is defined as:

```text
F(0) = 0
F(1) = 1
F(N) = F(N-1) + F(N-2), for N >= 2
```

## Input

A single integer `N`.

## Output

Print the `N`-th Fibonacci number modulo `1e9 + 7`.

## Constraints

```text
0 ≤ N ≤ 10^18
```

## Examples

### Example 1

**Input:**

```text
10
```

**Output:**

```text
55
```

### Example 2

**Input:**

```text
100
```

**Output:**

```text
687995182
```