# Round Robin

A computer has one processor and `n` processes, numbered 1 to `n`. All processes are ready at time 0. Process `i` needs `b_i` units of processor time to finish.

The processor uses **Round Robin** scheduling with a time slice of `q` units:

1. The processes wait in a queue, in the order `1, 2, ..., n`.
2. The process at the front of the queue runs for `min(q, remaining time)` units.
3. If the process still needs more time, it goes to the **back** of the queue.
4. If the process is finished, it leaves the queue. Its **end time** is the current time.
5. The next process starts right away. Switching between processes takes no time.

Find the end time of every process.

## Input Format

- The first line has two integers `n` and `q`.
- The second line has `n` space-separated integers `b_1, b_2, ..., b_n`.

## Constraints

- `1 <= n <= 1000`
- `1 <= q <= 1000`
- `1 <= b_i <= 1000`

## Output Format

Print `n` space-separated integers. The `i`-th integer is the end time of process `i`.

Note that the output is in order of process number, not in the order the processes finish.

## Sample Input 1

```
3 2
5 2 3
```

## Sample Output 1

```
10 4 9
```

## Explanation 1

The queue starts as P1, P2, P3 with remaining times 5, 2, 3.

- Time 0 → 2: P1 runs for 2 units. It has 3 left, so it goes to the back.
- Time 2 → 4: P2 runs for 2 units and finishes. Its end time is 4.
- Time 4 → 6: P3 runs for 2 units. It has 1 left, so it goes to the back.
- Time 6 → 8: P1 runs for 2 units. It has 1 left, so it goes to the back.
- Time 8 → 9: P3 runs for 1 unit and finishes. Its end time is 9.
- Time 9 → 10: P1 runs for 1 unit and finishes. Its end time is 10.

So the end times of P1, P2, P3 are 10, 4, 9.

## Sample Input 2

```
4 3
4 1 6 3
```

## Sample Output 2

```
11 4 14 10
```

## Explanation 2

The queue starts as P1, P2, P3, P4 with remaining times 4, 1, 6, 3.

- Time 0 → 3: P1 runs for 3 units. It has 1 left, so it goes to the back.
- Time 3 → 4: P2 needs only 1 unit, so it finishes early. Its end time is 4.
- Time 4 → 7: P3 runs for 3 units. It has 3 left, so it goes to the back.
- Time 7 → 10: P4 runs for 3 units and finishes. Its end time is 10.
- Time 10 → 11: P1 runs for 1 unit and finishes. Its end time is 11.
- Time 11 → 14: P3 runs for 3 units and finishes. Its end time is 14.

So the end times are 11, 4, 14, 10.
