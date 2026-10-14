# Valid Brackets

You are given a string that contains only the bracket characters `(`, `)`, `[`, `]`, `{` and `}`.

The string is **valid** if all of the following are true:

1. Every opening bracket is closed by a closing bracket of the same type: `(` by `)`, `[` by `]`, and `{` by `}`.
2. Brackets are closed in the correct order: the bracket that was opened most recently must be closed first.
3. Every closing bracket has a matching opening bracket before it, and every opening bracket is closed.

Print `YES` if the string is valid, otherwise print `NO`.

## Input Format

The only line contains the string, made of the characters `(`, `)`, `[`, `]`, `{` and `}`.

## Constraints

- `1 <= length of the string <= 10^6`

## Output Format

Print `YES` if the string is valid, otherwise print `NO`.

## Sample Input 1

```
()[]{}
```

## Sample Output 1

```
YES
```

## Explanation 1

Three pairs, each opened and closed in order.

## Sample Input 2

```
([)]
```

## Sample Output 2

```
NO
```

## Explanation 2

`[` was opened most recently, but `)` tries to close `(` first.

## Sample Input 3

```
{()[()]}
```

## Sample Output 3

```
YES
```

## Explanation 3

Everything inside `{ }` is valid, and `{ }` itself is closed correctly.

## Sample Input 4

```
((
```

## Sample Output 4

```
NO
```

## Explanation 4

The two opening brackets are never closed.
