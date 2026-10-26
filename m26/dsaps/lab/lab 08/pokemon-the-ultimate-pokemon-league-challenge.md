# Pokémon: The Ultimate Pokémon League Challenge!

Ash Ketchum is on a mission to become a Pokémon Master! But before he can challenge the Pokémon League, he needs to travel between different cities to meet Gym Leaders, collect badges, and occasionally stop Brock from getting distracted.

There are `n` cities in the Pokémon world, numbered from 0 to `n - 1`. The cities are connected by one-way routes, and each route has a travel cost representing the time Ash and Pikachu spend travelling.

Ash has a map of the Pokémon world, represented by an `n × n` adjacency matrix. The element at position `matrix[i][j]` represents the travel cost of the direct route from city `i` to city `j`.

- If `matrix[i][j] = -1`, there is no direct route between city `i` and city `j`.
- The diagonal elements represent the distance from a city to itself and are initially `0`.

Ash wants to determine the minimum travel cost between every pair of cities. Sometimes, travelling through other cities might be cheaper than taking a direct route.

For example, Ash might discover that travelling through Pewter City and Cerulean City is cheaper than taking a longer route directly to Vermilion City. Pikachu is happy because they can save time and reach the next Gym Battle sooner!

Your task is to help Ash calculate the shortest travel distances between every pair of cities and update the matrix accordingly.

If no path exists between two cities, the corresponding entry must remain `-1`.

Help Ash complete his journey and become a Pokémon Master without wasting unnecessary time travelling!

## Input Format

The first line contains an integer `n`, representing the number of cities.

The next `n` lines each contain `n` space-separated integers representing the adjacency matrix.

The integer at row `i`, column `j` represents the direct travel cost from city `i` to city `j`. A value of `-1` indicates that no direct route exists.

## Constraints

- `1 <= n <= 100`
- `-1 <= matrix[i][j] <= 1000`
- `matrix[i][i] = 0` for all `0 <= i < n`

## Output Format

Print the updated `n × n` matrix containing the shortest travel distances between every pair of cities.

- Print each row on a separate line.
- Separate elements within each row using spaces.
- If no path exists between two cities, print `-1` for that pair.

## Sample Input 1

```
4
0 2 -1 -1
1 0 3 -1
-1 -1 0 1
3 5 4 0
```

## Sample Output 1

```
0 2 5 6
1 0 3 4
4 6 0 1
3 5 4 0
```

## Explanation 1

Initially, the matrix contains only the direct travel costs between cities. Ash discovers that some journeys are cheaper when passing through intermediate cities.

- City 0 to City 2: Travel through City 1, with a total cost of 2 + 3 = 5.
- City 0 to City 3: Travel through Cities 1 and 2, with a total cost of 2 + 3 + 1 = 6.
- City 2 to City 0: Travel through City 3, with a total cost of 1 + 3 = 4.

After considering all possible routes, the matrix contains the minimum travel cost between every pair of cities.

Pikachu is thrilled that the team can reach their next destination faster!

## Sample Input 2

```
2
0 25
-1 0
```

## Sample Output 2

```
0 25
-1 0
```

## Explanation 2

There are only two cities. Ash can travel from City 0 to City 1 at a cost of 25, but there is no route from City 1 back to City 0.

Since no alternative route can improve the existing distances, the matrix remains unchanged.

Ash decides to move forward with his Pokémon journey instead of looking for a road that doesn't exist!

Ash's ultimate goal: Find the best routes, save valuable travel time, collect every Gym Badge, and become a Pokémon Master!
