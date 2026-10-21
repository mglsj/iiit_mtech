# High Scores

You play a game consisting of `n` rooms and `m` tunnels. Your initial score is 0, and each tunnel increases your score by `x` where `x` may be both positive or negative. You may go through a tunnel several times.

Your task is to walk from room 1 to room `n`. What is the maximum score you can get?

Note: If you can get an arbitrarily large score (i.e., there is a positive cycle reachable from 1 and can reach `n`), print `-1`.

## Input Format

- The first input line has two integers `n` and `m`: the number of rooms and tunnels.
- Then, there are `m` lines describing the tunnels. Each line has three integers `a`, `b`, and `x`:
  - Tunnel from room `a` to `b`, increases score by `x`.
- All tunnels are one-way.
- It is guaranteed that you can reach room `n` from room 1.

## Constraints

- `1 <= n <= 2500`
- `1 <= m <= 5000`
- `1 <= a, b <= n`
- `-10^9 <= x <= 10^9`

## Output Format

Print one integer:

- The maximum score you can achieve.
- Or `-1` if the score can be arbitrarily large.

## Sample Input 1

```
4 5
1 2 3
2 4 -1
1 3 -2
3 4 7
1 4 4
```

## Sample Output 1

```
5
```
