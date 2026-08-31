# Longest Common Substring

## Problem Statement

In this problem, you are given three strings `a`, `b`, and `c`, and the task is to find the **length of the longest common substring** that appears in all three strings.

A **substring** is a sequence of consecutive characters taken from a string, where the order of characters matters, and the sequence must be uninterrupted.

### Example of Substrings

For the string `"abcde"`, some of its substrings are:

- `"a"`
- `"ab"`
- `"abc"`
- `"bcd"`
- `"de"`

A substring must maintain the **order and continuity** of characters.

## Input Format

- The first line contains an integer `t`, which represents the number of test cases.
- The next `t * 3` lines contain the strings for each test case.
- Each test case is represented by **3 consecutive lines** of strings.

## Constraints

- `1 <= t <= 500`
- `1 <= |a|, |b|, |c| <= 100`

Here, `|s|` denotes the length of string `s`.

## Output Format

A single integer denoting the **length of the longest common substring** of the three strings.

## Sample Input 0

```text
2
abcdef
daxbyc
xyabzc
xabcy
abcxy
xyabc
```

## Sample Output 0

```text
1
3
```

## Explanation 0

- One of the common substrings is `"c"`, which appears in all three strings (`abcdef`, `daxbyc`, and `xyabzc`).
- The substring `"abc"` appears in all three strings (`xabcy`, `abcxy`, and `xyabc`).