from sudoku import Sudoku_Puzzle
from pprint import pprint
from timeit import default_timer as timer

''' test case used for development
unsolved:
[[5,3,None,None,7,None,None,None,None],
[6,None,None,1,9,5,None,None,None],
[None,9,8,None,None,None,None,6,None],
[8,None,None,None,6,None,None,None,3],
[4,None,None,8,None,3,None,None,1],
[7,None,None,None,2,None,None,None,6],
[None,6,None,None,None,None,2,8,None],
[None,None,None,4,1,9,None,None,5],
[None,None,None,None,8,None,None,7,9]]

solution:
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
'''



unsolved = [[5,3,None,None,7,None,None,None,None],
            [6,None,None,1,9,5,None,None,None],
            [None,9,8,None,None,None,None,6,None],
            [8,None,None,None,6,None,None,None,3],
            [4,None,None,8,None,3,None,None,1],
            [7,None,None,None,2,None,None,None,6],
            [None,6,None,None,None,None,2,8,None],
            [None,None,None,4,1,9,None,None,5],
            [None,None,None,None,8,None,None,7,9]]

'''
unsolved = [[None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None]]
'''
'''
unsolved = [[8,None,None,None,None,None,None,None,None],
            [None,None,3,6,None,None,None,None,None],
            [None,7,None,None,9,None,2,None,None],
            [None,5,None,None,None,7,None,None,None],
            [None,None,None,None,4,5,7,None,None],
            [None,None,None,1,None,None,None,3,None],
            [None,None,1,None,None,None,None,6,8],
            [None,None,8,5,None,None,None,1,None],
            [None,9,None,None,None,None,4,None,None]]
'''
'''
unsolved = [[1,2,3,4,5,6,7,8,None],
            [None,None,None,None,None,None,None,None,2],
            [None,None,None,None,None,None,None,None,3],
            [None,None,None,None,None,None,None,None,4],
            [None,None,None,None,None,None,None,None,5],
            [None,None,None,None,None,None,None,None,6],
            [None,None,None,None,None,None,None,None,7],
            [None,None,None,None,None,None,None,None,8],
            [None,None,None,None,None,None,None,None,9]]
'''

start = timer()
result = Sudoku_Puzzle.solve(unsolved, 0, 0)
end = timer()

if result:
  print("Puzzle is legal. Solution was found in " + str(round(end-start, 4)) + " seconds. Solution is:")
  pprint(unsolved)
else:
  print("Puzzle is not legal and cannot be solved. This was determined in " + str(round(end-start, 5)) + " seconds.")
