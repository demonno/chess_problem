from boards.chess_board import ChessBoard
from peaces.figures import Queen, Knight, King, Bishop

# b = ChessBoard(4, 4, [Rook(), Rook(), Knight(), Knight(), Knight(), Knight()])
# b = ChessBoard(3, 3, [Rook(), King(), King(), King()])

b = ChessBoard(7, 7, [Queen(), Queen(), Knight(), Bishop(), Bishop(), King(), King()])
b.solve()

print "Number of solutions", len(b.solutions)
for q in b.solutions:
    print q
