""" EIGHT QUEENS PUZZLE:

Problem: placing eight chess queens on an 8x8 chessboard so that no two
queens attack each other. Solution requires that no two queens share the
same row, column or diagonal.

Program: placing N queens on an NxN board - think about general cases, not just
8x8 case (ie: 12 queens on a 12x12 board, 30 queens on a 30x30 board).

Plan of Attack:
- Think about representation (data structure, ie: chessboard + queen)
- Once visualized, think about algorithm development (though not independent of representation)

Any solution to the N queens must be a permutation of the numbers [0...N-1]
"""
# start with equation for placement [0...N-1]
# generate various permutations 
# check each permutation for clashes (queens on the same diagonal)
# if no clashes, it's a solution --> print 

# diagonal has a slope of either 1 or -1
def share_diagonal(x0, y0, x1, y1):
    """ Test to see if two queens share a diagonal."""

    dy = abs(y1 - y0)   # abs value distance for y
    dx = abs(x1 - x0)   # abs value distance for x

    return dx == dy     # clash if dx == dy

# proceeding strategy:
# put 1 queen in first, put another in second colomn - though only if it doesn't clash
# put 3rd queen, checking against the first two queens to ensure no clashes

def col_clashes(bs, c):
    """ Return True if there is a column clash between queens."""

    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True 
    return False            # no clashes - c is safe



############################### TEST ###########################################

def test(did_pass):
    """ Tests for function calls."""

    linenum = sys._getframe(1).f_lineno # get the caller's line number
    if did_pass:
        msg = "Test at line {0} okay.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))

    print msg 

def test_suite():
    """ Run test suite for code."""

    test(not share_diagonal(5,2,2,0))
    test(share_diagonal(5,2,3,0))
    test(share_diagonal(5,2,4,3))
    test(share_diagonal(5,2,4,1))

    # Solutions cases that should not have any clashes
    test(not col_clashes([6,4,2,0,5], 4))
    test(not col_clashes([6,4,2,0,5,7,1,3], 7))

    # More test cases that should mostly clash
    test(col_clashes([0,1], 1))
    test(col_clashes([5,6], 1))
    test(col_clashes([6,5], 1))
    test(col_clashes([0,6,4,3], 3))
    test(col_clashes([5,0,7], 2))
    test(not col_clashes([2,0,1,3], 1))
    test(col_clashes([2,0,1,3], 2))

    test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
    test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
    test(has_clashes([0,1,2,3]))             # Try small 4x4 board
    test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case



