# Generate All Subsequences of a String

## Problem Statement

You are given a string `s` consisting of lowercase English letters.

Your task is to generate **all possible subsequences** of the string using backtracking.

- A **subsequence** of a string is formed by deleting zero or more characters from the string without changing the order of the remaining characters.
- The subsequences should be printed in **lexicographical order**.

---

## Input Format

A single line containing the string `s`.

---

## Output Format

Print all subsequences of the string, one per line, in **lexicographical order**.

---

## Constraints

- `1 ≤ |s| ≤ 15`
- `s` contains only lowercase English letters (`'a'` to `'z'`).

---

## Sample Testcases

### Sample Input 1

```text
abc
```

### Sample Output 1

```text
a
ab
abc
ac
b
bc
c
```

---

### Sample Input 2

```text
aa
```

### Sample Output 2

```text
a
aa
```

---

## Explanation

- In the first example, `"abc"` has `2^3 - 1 = 7` non-empty subsequences, printed in lexicographical order.
- In the second example, duplicate subsequences should **not** be repeated in the output.