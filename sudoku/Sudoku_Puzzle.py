# For more advanced approaches:
# https://github.com/mahdavipanah/SudokuPyCSF


class Sudoku:
    def __init__(self, puzzle=None):
        self.puzzle = puzzle

    def solve(self, row, col):
        """
        Finds and returns the solution to a sudoku puzzle
        :param puzzle: 2d list
        :param row: int
        :param col: int
        :return: 2d list of solved puzzle
        """
        # returns (row, col) of the next open position
        curr_location = self.find_unassigned_location(row)

        # None means no open position was found
        if curr_location[0] is not None:
            row = curr_location[0]
            col = curr_location[1]
            for num_to_try in range(1, 10):
                if self.is_safe(row, col, num_to_try):

                    # assign number tentatively
                    self.puzzle[row][col] = num_to_try

                    # make recursive call
                    if self.solve(row, col):
                        return True

                    # undo decision, previous decision did not work (backtrack)
                    self.puzzle[row][col] = None

        else:
            return True

        # puzzle was unsolvable
        return False

    def is_safe(self, row, col, num):
        """
        tests whether inserting a number at a position will violate sudoku constraints
        :param puzzle: 2d list
        :param row: int, vertical index of placement in question
        :param col: int, horizontal index of placement in question
        :param num: int, number being tested
        :return: T/F
        """
        if (not self.used_in_col(col, num)
           and not self.used_in_row(row, num)
           and not self.used_in_region(row - (row % 3), col - (col % 3), num)):
            return True
        else:
            return False

    def used_in_col(self, col, num):
        """
        checks if num is already present in the column
        :param puzzle: 2d list
        :param col: int, horizontal index of placement in question
        :param num: int, number being tested
        :return: T/F
        """
        for current_row in self.puzzle:
            if current_row[col] == num:
                return True

        return False

    def used_in_row(self, row, num):
        """
        checks if num is already present in the row
        :param puzzle: 2d list
        :param row: int, vertical index of placement in question
        :param num: int, number being tested
        :return: T/F
        """
        for current_col in self.puzzle[row]:
            if current_col == num:
                return True

        return False

    def used_in_region(self, region_start_row, region_start_col, num):
        """
        checks if num is already present in the 3x3 region of the coord
        :param puzzle: 2d list
        :param region_start_row: int, indx of top row of 3x3 region of coord
        :param region_start_col: int, indx of left col of 3x3 region of coord
        :param num: int, number being tested
        :return: T/F
        """
        for current_row in range(0, 3):
            for current_col in range(0, 3):
                if self.puzzle[region_start_row + current_row][region_start_col + current_col] == num:
                    return True

        return False

    def find_unassigned_location(self, row):
        """
        finds the next open(None) location in 2d list
        :param puzzle: 2d list
        :param row: int, current coordinate
        :return: (int,int) of next unassigned index. (None,None) if no open position
        """
        for ind_row, y in enumerate(self.puzzle[row:], start=row):
            for x in range(len(y)):  # TODO: inefficient iteration
                if self.puzzle[ind_row][x] is None:
                    return (ind_row, x)

        # no unassigned locations
        return (None, None)

    def set_puzzle(self, pz):
        self.puzzle = pz

    def get_puzzle(self):
        return self.puzzle
