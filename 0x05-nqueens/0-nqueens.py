#!/usr/bin/python3
"""
0-nqueens.py
"""
import sys


def queens(n, row=0, p=[], tl=[], tr=[]):
    """
    find possible position of queens on a
    chess board
    n: size of board (nxn)
    row: the current row
    p: current placement of queens
    tl: diagonals from top-left to bottom-right
    tr: diagonals from top-right to bottom-left
    """
    if row < n:
        for col in range(n):
            cond0 = row + col not in tl
            cond1 = row - col not in tr
            if col not in p and cond0 and cond1:
                new_tl = tl + [row + col]
                new_tr = tr + [row - col]
                yield from queens(n, row+1, p+[col], new_tl, new_tr)
    else:
        yield p


def nqueens(n):
    """
    solve the N-queens puzzle
    """
    result = []
    i = 0
    for res in queens(n, 0):
        for val in res:
            result.append([i, val])
            i += 1
        print(result)
        result = []
        i = 0


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    n = int(sys.argv[1])
    nqueens(n)
