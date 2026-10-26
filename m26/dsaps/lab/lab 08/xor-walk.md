# XOR Walk

Alice is playing a game on a tree with `n` vertices, numbered 1 to `n`. Every edge of the tree has a weight.

Alice starts at vertex `a`. She has a number `x`, which is 0 at the start. Her goal is to reach the treasure, which is at vertex `b`.

The rules of the game:

- **Moving.** Alice can move from her vertex to a neighbouring vertex along an edge. If the edge has weight `w`, then `x` becomes `x ⊕ w`, where `⊕` is the bitwise XOR operation.
- **The treasure room is locked.** Alice can enter vertex `b` only if `x = 0` right after the move. If `x` would not be 0, she is not allowed to make that move.
- **Teleport.** Alice has a teleport. She can use it **at most once**, at any time (even before her first move), or she can skip it. It takes her to **any vertex except** `b`, and `x` does not change.

Alice can use the same edge as many times as she wants.

Can Alice reach the treasure at vertex `b`?

## Input Format

- The first line has an integer `t`, the number of test cases.
- Each test case starts with a line with three integers `n`, `a` and `b`.
- The next `n - 1` lines each have three integers `u`, `v` and `w`. This means there is an edge between vertices `u` and `v` with weight `w`.

## Constraints

- `1 <= t <= 1000`
- `2 <= n <= 10^5`
- `1 <= a, b <= n`, `a != b`
- `1 <= w <= 10^9`
- The sum of `n` over all test cases is at most `10^5`.
- The edges always form a tree.

## Output Format

For each test case, print `YES` if Alice can reach vertex `b`, otherwise print `NO`.

## Sample Input 1

```
3
3 1 3
1 2 5
2 3 5
3 1 3
1 2 4
2 3 6
5 1 4
1 2 1
2 3 2
3 4 4
1 5 4
```

## Sample Output 1

```
YES
NO
YES
```

## Explanation 1

**Test 1.** Alice moves 1 → 2, so x = 5. Then she moves 2 → 3, so x = 5 ⊕ 5 = 0. She enters vertex 3 with x = 0. The answer is `YES`, and she does not need the teleport.

**Test 2.** If Alice moves 1 → 2 → 3, then x = 4 ⊕ 6 = 2 when she arrives at vertex 3, so she cannot enter.

The teleport does not help. Before teleporting, x can only be 0 (at vertex 1) or 4 (at vertex 2). After teleporting to vertex 1, she needs x = 2 to enter. After teleporting to vertex 2, she needs x = 6. She cannot get either, so the answer is `NO`.

**Test 3.** Alice moves 1 → 2 → 3, so x = 1 ⊕ 2 = 3. She teleports to vertex 5, and x stays 3. Then she moves:

- 5 → 1: x = 3 ⊕ 4 = 7
- 1 → 2: x = 7 ⊕ 1 = 6
- 2 → 3: x = 6 ⊕ 2 = 4
- 3 → 4: x = 4 ⊕ 4 = 0

She enters vertex 4 with x = 0, so the answer is `YES`.
