# Max of min for every window size

You are given an integer array `arr[]`. The task is to find the **maximum of minimum** values for every window size `k` where `1 <= k <= arr.size()`.

For each window size `k`:

- Consider all contiguous subarrays of length `k`.
- Determine the minimum element in each subarray.
- Then, take the maximum among all these minimums.

Return the results as an array, where the element at index `i` represents the answer for window size `i + 1`.

## Input Format

1. An integer `n` — the size of the array.
2. `n` space-separated integers representing the array elements.

## Constraints

- `1 <= arr.size() <= 10^5`
- `1 <= arr[i] <= 10^6`

## Output Format

Print `n` integers — the result array. The element at index `i` corresponds to the maximum of minimums for window size `i + 1`.

## Sample Input 1

```
7
10 20 30 50 10 70 30
```

## Sample Output 1

```
70 30 20 10 10 10 10
```

## Explanation 1

- Window size = 1 → max of minimums = 70
- Window size = 2 → max of minimums = 30
- Window size = 3 → max of minimums = 20
- ... and so on.

## Sample Input 2

```
3
10 20 30
```

## Sample Output 2

```
30 20 10
```

## Explanation 2

- Window size = 1 → max of minimums = 30
- Window size = 2 → max of minimums = 20
- Window size = 3 → max of minimums = 10
