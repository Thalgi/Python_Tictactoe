from src.user import User
from src.gameboard import Gameboard

def tic_tac_toe():
    board = Gameboard()
    player_x = User('X')
    player_o = User('O')
    current_player = player_x

    while True:
        board.show_board()
        print(f"Player {current_player.marker}'s turn")

        row, col = current_player.get_move()

        if board.is_move_valid(row, col):
            board.do_move(row, col, current_player.marker)

            if board.check_winner(current_player.marker):
                board.show_board()
                print(f"Player {current_player.marker} wins!")
                break

            # Check for a draw after every move
            draw = all(board.is_move_valid(i, j) is False for i in range(3) for j in range(3))
            if draw:
                board.show_board()
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = player_o if current_player == player_x else player_x
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
