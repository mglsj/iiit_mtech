# Maximum Activities

## Problem Statement

You are the manager of a very busy event hall and have received **N** requests to book the hall for an activity. Each request `i` has a specific **start time** `Sᵢ` and an **end time** `Eᵢ`.

Your task is to determine the maximum number of activities you can schedule in the hall. The only constraint is that you can only host **one activity at a time**.

An activity can begin at the exact moment another one ends. For example, an activity ending at 5 PM is not considered to overlap with an activity starting at 5 PM.

## Input Format

- The first line contains a single integer `N`, the total number of activity requests.
- The next `N` lines each contain two space-separated integers `Sᵢ` and `Eᵢ`, representing the start and end time of the `i`-th activity.

## Output Format

Print a single integer representing the maximum number of activities that can be scheduled.

## Constraints

- `1 ≤ N ≤ 10⁵`
- `0 ≤ Sᵢ < Eᵢ ≤ 10⁹`

## Sample Input 1

```text
6
1 3
2 5
3 4
5 7
8 9
6 10
```

## Sample Output 1

```text
4
```

### Explanation

One optimal solution is to select the activities scheduled for:

- `(1, 3)`
- `(3, 4)`
- `(5, 7)`
- `(8, 9)`

This gives a total of **4** non-overlapping activities.

## Sample Input 2

```text
3
10 20
12 15
20 30
```

## Sample Output 2

```text
2
```

### Explanation

You can select activities `(10, 20)` and `(20, 30)`.

Notice that you cannot select `(12, 15)` if you select `(10, 20)`.