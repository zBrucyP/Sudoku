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

# base test case
unsolved1 = [[5,3,None,None,7,None,None,None,None],
            [6,None,None,1,9,5,None,None,None],
            [None,9,8,None,None,None,None,6,None],
            [8,None,None,None,6,None,None,None,3],
            [4,None,None,8,None,3,None,None,1],
            [7,None,None,None,2,None,None,None,6],
            [None,6,None,None,None,None,2,8,None],
            [None,None,None,4,1,9,None,None,5],
            [None,None,None,None,8,None,None,7,9]]

# test empty puzzle
unsolved2 = [[None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None]]

# test a "hard" puzzle
unsolved3 = [[8,None,None,None,None,None,None,None,None],
            [None,None,3,6,None,None,None,None,None],
            [None,7,None,None,9,None,2,None,None],
            [None,5,None,None,None,7,None,None,None],
            [None,None,None,None,4,5,7,None,None],
            [None,None,None,1,None,None,None,3,None],
            [None,None,1,None,None,None,None,6,8],
            [None,None,8,5,None,None,None,1,None],
            [None,9,None,None,None,None,4,None,None]]

# test unsolvable puzzle (0 legal solutions)
unsolved4 = [[1,2,3,4,5,6,7,8,None],
            [None,None,None,None,None,None,None,None,2],
            [None,None,None,None,None,None,None,None,3],
            [None,None,None,None,None,None,None,None,4],
            [None,None,None,None,None,None,None,None,5],
            [None,None,None,None,None,None,None,None,6],
            [None,None,None,None,None,None,None,None,7],
            [None,None,None,None,None,None,None,None,8],
            [None,None,None,None,None,None,None,None,9]]

# gather full list of unsolved puzzles
unsolved_puzzles = []
unsolved_puzzles.append(unsolved1)
unsolved_puzzles.append(unsolved2)
unsolved_puzzles.append(unsolved3)
unsolved_puzzles.append(unsolved4)

# iterate through tests, time entire test
start_of_testing = timer()
for puzzle in unsolved_puzzles:
    # print the initial puzzle
    print('\n\nPuzzle:')
    pprint(puzzle)

    # setup sudoku object and timers. Run the solve function for puzzle
    sudoku_puzzle = Sudoku_Puzzle.Sudoku(puzzle)
    test_case_start = timer()
    result = sudoku_puzzle.solve(0,0)
    test_case_end = timer()
    print('===')

    # if solution is possible or not
    if result:
        print('Puzzle is legal. Solution was found in ' + str(round(test_case_end-test_case_start,4)) + ' seconds. Solution is:')
        pprint(sudoku_puzzle.get_puzzle())
    else:
        print('Puzzle is not legal and cannot be solved. This was determined in ' + str(round(test_case_end-test_case_start,7)) + ' seconds.')

end_of_testing = timer()
print('---------------')
print('\nTesting has ended. It took a total of ' + str(round(end_of_testing-start_of_testing,4)) + ' seconds, with an average solve time of ' + str(round((end_of_testing-start_of_testing)/len(unsolved_puzzles),4)) + ' seconds.')
