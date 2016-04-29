from boards.chess_board import ChessBoard
from pieces.pieces import Rook, King

board = ChessBoard(3, 3, [King(), King(), Rook()])
board.solve()
board.print_solutions(include_quantity=True)
