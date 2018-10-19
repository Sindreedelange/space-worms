from Board import Board


def main():
    board = Board()
    board.populate_board()
    for square in board.squares:
        print("Main method: ", square.number)

main()

