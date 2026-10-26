# Optimize Snakes & Ladders Game

In the free time Habibi takes out his Snakes and Ladders Game, stares at the board and wonders: "If I can always roll the die to whatever number I want, what would be the least number of rolls to reach the destination?"

**Rules:**

- The game is played with cubic dice of 6 faces numbered from **1** to **6**.
- Starting from **1**, land on square **100** with the exact roll of the die. If moving the number rolled would place the player beyond square **100**, no move is made.
- If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.
- If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.

**Board description:**

- The board is always **10 x 10** with squares numbered from **1** to **100**.
- The board contains `n` ladders given in a form of a **2D matrix** `ladders` of size `n * 2` where `(ladders[i][0], ladders[i][1])` denotes a ladder that has its base on square `ladders[i][0]` and end at square `ladders[i][1]`.
- The board contains `m` snakes given in a form of a **2D matrix** `snakes` of size `m * 2` where `(snakes[i][0], snakes[i][1])` denotes a snake that has its mouth on square `snakes[i][0]` and tail at square `snakes[i][1]`.

## Input Format

- First line contains `n` and `m`, size of **2D matrix** `ladders` and `snakes` respectively.
- The next `n` lines contain the start and end positions of the ladders on the board, i.e., `ladders[i][0], ladders[i][1]`.
- The next `m` lines contain the start and end positions of the snakes on the board, i.e., `snakes[i][0], snakes[i][1]`.

## Constraints

- `1 <= n, m <= 15`
- `1 <= ladders[i][0], ladders[i][1], snakes[i][0], snakes[i][1] <= 100`
- `ladders[i][0] < ladders[i][1]` and `snakes[i][0] > snakes[i][1]`
- Neither square 1 nor square 100 will be the starting point of a ladder or snake.
- A square will have at most one endpoint from either a snake or a ladder.

## Output Format

- Return the **least number of rolls** to move from start to finish on a separate line. If there is **no solution**, return `-1`.

## Sample Input 1

```
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
```

## Sample Output 1

```
3
```

## Explanation 1

The player can roll a 5 and a 6 to land at square 12. There is a ladder to square 98. A roll of 2 ends the traverse in 3 rolls.
