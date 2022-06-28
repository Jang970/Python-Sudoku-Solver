# create a sudoku solver using recursion/backtracking
# our puzzle will be passed in as a list of lists, where each inner list represents a row in the puzzle
# empty spaces are represented by -1 in our puzzle

def findEmptySlot(puzzle):
    # function will find the next row, col in our puzzle that is not filled
    # empty spaces are represented by -1 in our puzzle

    # iterate through all of our puzzle's rows and cols, 9x9 matrix
    for r in range(9): # going from 0 to 8
        for c in range(9): 

            # if an empty slot is found, return respective indicies
            # will return first empty slot found
            if puzzle[r][c] == -1:
                return r, c
        

    # otherwise, there are no more empty slots, puzzle is full, we can then return NONE, NONE
    return None, None

def isValid(puzzle, guess, row, col):

    # for guess to be valid, it must be the only number in its respective row, col and its 3x3 matrix
    # return True if valid

    # check row validity
    # get all values of our specific row in our puzzle
    rowVals = puzzle[row]

    if guess in rowVals:

        # if our guess is in those row values, then our guess is invalid
        return False

    # check column validity
    # create a new list to contain all column values
    # to get column values, we iterate through all rows in specific column in our puzzle
    colVals = []

    for i in range(9): # iterating through all rows

        # fill our list
        colVals.append(puzzle[i][col])
        
    if guess in colVals:

        return False    

    # now for 3x3 matrix find where it starts and then iterate over its 3 values in row/col
    # can take row/col index and divide by 3 and throw away remainder, this will tell us which 3x3 square we are working with in our puzzle
    # for eg if row // 3 = 0, we are in the top part of our 9x9 matrix
    # if col // 3 = 2, then we are in the top row, last column 3x3 in our puzzle
    # multiply by 3 to get actual index
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    # now we want to iterate through whole 3x3 square
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):

            # check if guess is in the 3x3 square already
            if puzzle[r][c] == guess:

                return False


    # if we pass all these checks, guess is valid 
    return True            

def solveSudoku(puzzle):

    # this function takes in the puzzle as the input and will return if a solution exists or not
    # it will also make changes to the puzzle in order to create a solution if it exists

    # first step is to choose somewhere in the puzzle to make a guess
    # call a helper function that will return the row and column indicies of an empty slot in our puzzle
    row, col = findEmptySlot(puzzle)

    # validation checks to see if our guess is correct

    # first check if row == None, it means all slots are filled and so our puzzle is solved, thus we return True
    if row is None:
        return True
    
    # otherwise, if there is a an empty slot, then we make a guess using numbers between 1 and 9
    # we want to check and use each number 
    for guess in range(1, 10): # goes from 1 to 9

        # for each guess, we want to check if it is a valid one
        # use helper function
        if isValid(puzzle, guess, row, col):
            
            # if the guess is valid, then we place the guess in that slot in our puzzle
            puzzle[row][col] = guess

            # now recursively call function
            if solveSudoku(puzzle):

                # if with our guess solveSudoku returns true, then we know we have solved our puzzle
                return True

        # if the guess is not valid or does not solve our puzzle, then we must backtrack
        puzzle[row][col] = -1 # reset to move to next guess


    # if we have tried every guess and none work, then our puzzle is unsolvable, we then return false
    return False    


# main function... test case
exampleBoard = [
    [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
    [-1, -1, -1,  2, -1, -1,  -1, -1 ,5],
    [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

    [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
    [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
    [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

    [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
    [6, 7, -1,  1, -1, 5,  -1, 4, -1],
    [1, -1, 9,  -1, -1, -1,  2, -1, -1]
]

print(solveSudoku(exampleBoard))
print(exampleBoard)