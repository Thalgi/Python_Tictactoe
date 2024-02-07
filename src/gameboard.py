import tkinter as tk


class Gameboard_OLD:

    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

    def show_board(self):
        for row in self.board:
            print('   |   '.join(row))
            print('-' * 17)
        print("       0       1       2")

    def is_move_valid(self, row, col):
        return self.board[row][col] == ''

    def do_move(self, row, col, marker):
        self.board[row][col] = marker

    def check_winner(self, marker):
        for i in range(3):
            if all(self.board[i][j] == marker for j in range(3)) or all(self.board[j][i] == marker for j in range(3)):
                return True

        if all(self.board[i][i] == marker for i in range(3)) or all(self.board[i][2 - i] == marker for i in range(3)):
            return True

        return False


class GameBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.geometry("300x300")

        self.start_frame = tk.Frame(self)
        self.start_frame.pack()

        start_label = tk.Label(self.start_frame, text="Welcome to Tic-Tac-Toe", font=('Helvetica', 16))
        start_label.pack(pady=10)

        start_button = tk.Button(self.start_frame, text="Start Game", command=self.show_game_board)
        start_button.pack()

        self.retry_frame = tk.Frame(self)
        self.retry_frame.pack()

        retry_label = tk.Label(self.retry_frame, text="", font=('Helvetica', 16))
        retry_label.pack(pady=10)

        retry_button = tk.Button(self.retry_frame, text="Retry", command=self.reset_game)
        retry_button.pack()

        self.game_frame = tk.Frame(self)
        self.game_frame.pack()

        self.board_buttons = [[None, None, None] for _ in range(3)]
        self.current_player = 'X'
        self.create_board_buttons()

        self.show_start_screen()

    def create_board_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.game_frame, text="", font=('Helvetica', 24), width=3, height=1,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.board_buttons[i][j] = button

    def show_start_screen(self):
        self.game_frame.pack_forget()
        self.retry_frame.pack_forget()
        self.start_frame.pack()

    def show_game_board(self):
        self.start_frame.pack_forget()
        self.retry_frame.pack_forget()
        self.game_frame.pack()

    def show_retry_screen(self, message):
        self.start_frame.pack_forget()
        self.game_frame.pack_forget()
        self.retry_frame.pack()

        retry_label = self.retry_frame.winfo_children()[0]
        retry_label.config(text=message)

    def on_button_click(self, row, col):
        if self.board_buttons[row][col]["text"] == "" and not self.check_winner():
            self.board_buttons[row][col]["text"] = self.current_player

            if self.check_winner():
                self.display_winner()
            elif self.check_draw():
                self.display_draw()
            else:
                self.switch_player()

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if all(self.board_buttons[i][j]["text"] == self.current_player for j in range(3)) or all(
                    self.board_buttons[j][i]["text"] == self.current_player for j in range(3)):
                return True

        # Check diagonals
        if all(self.board_buttons[i][i]["text"] == self.current_player for i in range(3)) or all(
                self.board_buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board_buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def display_winner(self):
        self.show_retry_screen(f"Player {self.current_player} wins!")

    def display_draw(self):
        self.show_retry_screen("It's a draw!")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board_buttons[i][j]["text"] = ""
                self.board_buttons[i][j]["state"] = tk.NORMAL

        self.current_player = 'X'
        self.show_game_board()
