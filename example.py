import time
from boards.chess_board import ChessBoard
from pieces.pieces import Rook, King, Queen, Bishop, Knight

# board = ChessBoard(3, 3, [King(), King(), Rook()])
# board.solve()
# board.print_solutions(include_quantity=True)

# 7 7 board with 2 Kings, 2 Queens, 2 Bishops and 1 Knight.
# Also provide the time it took to get the final score. Needless to say, the lower the time, the better.

start_time = time.time()
board = ChessBoard(7, 7, [King(), King(), Queen(), Queen(), Bishop(), Bishop(), Knight()])
board.solve()

print "Total Number of unique configurations %s " % board.number_of_solutions()
print "Time for solving problem %s seconds" % (time.time() - start_time)
