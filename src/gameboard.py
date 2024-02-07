class Gameboard:

    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

    def show_board(self):
        for row in self.board:
            print('   |   '.join(row))
            print('-' * 17)
        print("       0       1       2")

    def is_move_valid(self,row ,col):
        return self.board[row][col] == ''

    def do_move(self,row,col,marker):
        self.board[row][col] = marker

    def check_winner(self, marker):
        for i in range(3):
            if all(self.board[i][j] == marker for j in range(3)) or all(self.board[j][i] == marker for j in range(3)):
                return True

        if all(self.board[i][i] == marker for i in range(3)) or all(self.board[i][2 - i] == marker for i in range(3)):
            return True

        return False
