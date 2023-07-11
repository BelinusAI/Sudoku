# Sudoku
Program to solve Sudoku puzzles using backtracking recursive structure.

I representing the board as a list of lists, each grid cell holding an assigned digit. I use the digit 0 to indicate that a cell has not yet been filled. The solution to a Sudoku puzzle is just such a grid, but one in which no 0 entries remain and all the constraints are satisfied.


+---+---+---+ <br>
|517|6  | 34|
|289|  4|   |
|346|2 5| 9 |
+---+---+---+
|6 2|   | 1 |
| 38|  6| 47|
|   |   |   |
+---+---+---+
| 9 |   | 78|
|7 3|4  |56 |
|   |   |   |
+---+---+---+

+---+---+---+
|517|698|234|
|289|134|756|
|346|275|891|
+---+---+---+
|672|849|315|
|138|526|947|
|954|713|682|
+---+---+---+
|495|362|178|
|723|481|569|
|861|957|423|
+---+---+---+
0.002999544143676758 seconds
