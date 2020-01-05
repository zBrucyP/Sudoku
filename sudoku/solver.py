from pprint import pprint
from timeit import default_timer as timer
#For more advanced approaches:
#https://github.com/mahdavipanah/SudokuPyCSF

def solve(puzzle, row, col):
  """
  Finds and returns the solution to a sudoku puzzle
  :param puzzle: 2d list
  :param row: int
  :param col: int
  :return: 2d list of solved puzzle
  """
  # returns (row, col) of the next open position
  curr_location = find_unassigned_location(puzzle, row, col)

  # None means no open position was found
  if curr_location[0] is not None:
    row = curr_location[0]
    col = curr_location[1]
    for num_to_try in range(1,10):
      if is_safe(puzzle, row, col, num_to_try):

        # assign number tentatively
        puzzle[row][col] = num_to_try

        # make recursive call
        if solve(puzzle, row, col):
          return True

        # undo decision, previous decision did not work (backtrack)
        puzzle[row][col] = None

  else:
    return True

  # puzzle was unsolvable
  return False

def is_safe(puzzle, row, col, num):
  """
  tests whether inserting a number at a position will violate sudoku constraints
  :param puzzle: 2d list
  :param row: int, vertical index of placement in question
  :param col: int, horizontal index of placement in question
  :param num: int, number being tested
  :return: T/F
  """
  if not used_in_col(puzzle, col, num) and not used_in_row(puzzle, row, num) and not used_in_region(puzzle, row - (row % 3), col - (col % 3), num):
    return True
  else:
    return False

def used_in_col(puzzle, col, num):
  """
  checks if num is already present in the column
  :param puzzle: 2d list
  :param col: int, horizontal index of placement in question
  :param num: int, number being tested
  :return: T/F
  """
  for current_row in puzzle:
    if current_row[col] == num:
      return True

  return False

def used_in_row(puzzle, row, num):
  """
  checks if num is already present in the row
  :param puzzle: 2d list
  :param row: int, vertical index of placement in question
  :param num: int, number being tested
  :return: T/F
  """
  for current_col in puzzle[row]:
    if current_col == num:
      return True

  return False

def used_in_region(puzzle, region_start_row, region_start_col, num):
  """
  checks if num is already present in the 3x3 region of the coord
  :param puzzle: 2d list
  :param region_start_row: int, indx of top row of 3x3 region of coord
  :param region_start_col: int, indx of left col of 3x3 region of coord
  :param num: int, number being tested
  :return: T/F
  """
  for current_row in range(0,3):
    for current_col in range(0,3):
      if puzzle[region_start_row + current_row][region_start_col + current_col] == num:
        return True

  return False

def find_unassigned_location(puzzle, row, col):
  """
  finds the next open(None) location in 2d list
  :param puzzle: 2d list
  :param row: int, current coordinate
  :param col: int, current coordinate
  :return: (int,int) of next unassigned index. (None,None) if no open position
  """
  for ind_row, y in enumerate(puzzle[row:], start=row):
    for x in range(len(y)): # TODO: inefficient iteration
      if puzzle[ind_row][x] is None:
        return (ind_row,x)

  # no unassigned locations
  return (None,None)


''' test case used for development
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
result = solve(unsolved, 0, 0)
end = timer()

if result:
  print("Puzzle is legal. Solution was found in " + str(round(end-start, 4)) + " seconds. Solution is:")
  pprint(unsolved)
else:
  print("Puzzle is not legal and cannot be solved. This was determined in " + str(round(end-start, 5)) + " seconds.")
