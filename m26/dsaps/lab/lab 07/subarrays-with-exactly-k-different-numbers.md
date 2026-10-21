# Subarrays with Exactly K Different Numbers

You are given an array `A` of `N` integers and an integer `K`.

A **subarray** is a part of the array made of one or more consecutive elements.

Count the number of subarrays that contain **exactly** `K` different numbers.

For example, the subarray `[1, 2, 1, 3]` contains 3 different numbers: 1, 2 and 3.

## Input Format

The first line contains two integers `N` and `K`.

The second line contains `N` integers `A[1], A[2], ..., A[N]`.

## Constraints

- `1 <= N <= 2 * 10^5`
- `1 <= K <= N`
- `1 <= A[i] <= N`

## Output Format

Print a single integer — the number of subarrays with exactly `K` different numbers.

## Sample Input 1

```
5 2
1 2 1 2 3
```

## Sample Output 1

```
7
```

## Explanation 1

The subarrays with exactly 2 different numbers are:

`[1, 2]`, `[2, 1]`, `[1, 2]`, `[2, 3]`, `[1, 2, 1]`, `[2, 1, 2]` and `[1, 2, 1, 2]`.

There are 7 of them.

## Sample Input 2

```
5 3
1 2 1 3 4
```

## Sample Output 2

```
3
```

## Explanation 2

The subarrays with exactly 3 different numbers are `[1, 2, 1, 3]`, `[2, 1, 3]` and `[1, 3, 4]`.

## Sample Input 3

```
4 3
2 2 2 2
```

## Sample Output 3

```
0
```

## Explanation 3

The whole array contains only one different number, so no subarray can contain 3 different numbers.
