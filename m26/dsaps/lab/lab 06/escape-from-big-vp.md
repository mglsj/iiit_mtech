# Escape from Big VP

It's 11 PM in OBH (Old Boys Hostel), and Big VP has struck again. Not content with flooding the OBH WhatsApp group and spamming every Life mailing list in IIIT, he has now decided to read out his latest "important announcement" in person. Big VP has posted his loyal followers in some of the rooms, and they will drag every student they can trap straight to his room for the reading.

OBH is a grid of rooms with `R` rows and `C` columns. Every room has either a normal Student (`S`) or one of Big VP's followers (`V`).

Students in rooms that are next to each other up, down, left or right (not diagonally) are friends and stick together as one **gang**. Friendships chain: if A is next to B and B is next to C, then A, B and C are all in the same gang.

A gang is **trapped** if every room directly up, down, left or right of the gang is a `V` room. In the picture below, the gang (`S`) is trapped only if every room marked `*` is a `V` room. Rooms marked `.` don't touch the gang, so they don't matter.

```
. * * .
* S S *
. * S *
. . * .
```

One catch: students in rooms on the outer edge of OBH can always jump out of the window. There are no followers outside the hostel, so a gang with even one member in an edge room **escapes**.

Every trapped gang gets dragged to Big VP's room. How many students escape?

## Input Format

The first line contains two integers `R` and `C`, the number of rows and columns.

Each of the next `R` lines contains a string of exactly `C` characters, each either `S` or `V`.

## Constraints

- `1 <= R, C <= 500`
- Every character of the grid is either `S` or `V`

## Output Format

Print a single integer: the number of students who escape.

## Sample Input 1

```
4 4
VVVV
VSSV
VVSV
VSVV
```

## Sample Output 1

```
1
```

## Explanation 1

The students at (2, 2), (2, 3) and (3, 3) form one gang, and it is boxed in by followers on every side. All three get dragged to Big VP's room.

The student at (4, 2) is in an edge room and jumps out of the window. The answer is `1`.

## Sample Input 2

```
5 5
VVVVV
VSSSV
VSVSV
VSSSV
VVSVV
```

## Sample Output 2

```
9
```

## Explanation 2

All 9 students form one big gang. The student at (5, 3) is in an edge room, so the whole gang escapes through that window. The answer is `9`.

## Sample Input 3

```
4 4
SVVV
VSVV
VVSV
VVVV
```

## Sample Output 3

```
1
```

## Explanation 3

The students at (2, 2) and (3, 3) only touch each other diagonally, so they are not friends. Each one is a gang of one, each is boxed in by followers, and both get dragged to Big VP's room.

The student at (1, 1) is in an edge room and escapes. The answer is `1`.
