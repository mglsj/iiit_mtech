# HelpAlex

As soon as biometric attendance is done, Alex, a student, is trying to sneak out of the DSAPS class. Help your friend Alex escape safely! The college management appointed monsters to patrol the classroom and catch any student trying to leave early.

Alex and some monsters are in a labyrinth. When taking a step to some direction in the labyrinth, each monster may simultaneously take one as well. Your goal is to reach one of the boundary squares without ever sharing a square with a monster.

Both Alex and the monsters can traverse the labyrinth in four directions (Up, Down, Left, Right).

Your task is to find out if your goal is possible, and if it is, print `YES`, else `NO`. Your plan has to work in any situation; even if the monsters know your path beforehand.

## Input Format

- The first input line has two integers `n` and `m`: the height and width of the map.
- After this there are `n` lines of `m` characters describing the map. Each character is:
  - `.` — floor
  - `#` — wall
  - `A` — start
  - `M` — monster
- There is exactly one `A` in the input.

## Constraints

- `1 <= n, m <= 1000`

## Output Format

- First print `YES` if your goal is possible, and `NO` otherwise.

## Sample Input 1

```
5 8
########
#M..A..#
#.#.M#.#
#M#..#..
#.######
```

## Sample Output 1

```
YES
```

## Explanation 1

One of the possible paths is `RRDDR`: right, right, down, down, right.
