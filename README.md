[![Build Status](https://travis-ci.org/demonno/chess_problem.svg?branch=master)](https://travis-ci.org/demonno/chess_problem) [![Coverage Status](https://coveralls.io/repos/github/demonno/chess_problem/badge.svg?branch=master)](https://coveralls.io/github/demonno/chess_problem?branch=master)

# Chess Challenge

## Problem


The problem is to find all unique configurations of a set of normal 
chess pieces on a chess board with dimensions `M×N` where none of the 
pieces is in a position to take any of the others. Assume the colour 
of the piece does not matter, and that there are no pawns among 
the pieces.

Write a program which takes as input:

* The dimensions of the board: `M`, `N`
* The number of pieces of each type (`King`, `Queen`, `Bishop`, `Rook` 
and `Knight`) to try and place on the board.

As output, the program should list all the unique configurations to the 
console for which all of the pieces can be placed on the board without 
threatening each other.

## Examples

Input: `3×3` board containing `2 Kings` and `1 Rook`.

Output:


    K . .  |  . R .  |  . . K  |  K . K 
    . . R  |  . . .  |  R . .  |  . . .
    K . .  |  K . K  |  . . K  |  . R . 
 

Input: `4×4` board containing `2 Rooks` and `4 Knights`.

Output:

    . . . R  |  . N . N  |  . N . N  |  N . N . 
    N . N .  |  . . R .  |  R . . .  |  . . . R 
    . R . .  |  . N . N  |  . N . N  |  N . N . 
    N . N .  |  R . . .  |  . . R .  |  . R . . 


    . R . .  |  R . . .  |  N . N .  |  . . R . 
    N . N .  |  . N . N  |  . R . .  |  . N . N 
    . . . R  |  . . R .  |  N . N .  |  R . . . 
    N . N .  |  . N . N  |  . . . R  |  . N . N 

Solve first example

    from boards.chess_board import ChessBoard
    from pieces.pieces import Rook, King
    
    board = ChessBoard(3, 3, [King(), King(), Rook()])
    board.solve()
    board.print_solutions(include_quantity=True)

Solve second example

    from boards.chess_board import ChessBoard
    from pieces.pieces import Knight, Rook
    
    board = ChessBoard(4, 4, [Rook(), Rook(), Knight(), Knight(), Knight(), Knight()])
    board.solve()
    board.print_solutions(include_quantity=True)

Install Requirements

    pip install -r requirements.txt

Run tests using nose

    nosetests --with-coverage --cover-erase --cover-package=boards,pieces --cover-html

# TODO

* add automatic instantiating of pieces











 
