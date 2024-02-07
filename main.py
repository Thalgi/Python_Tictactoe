"""
Simple Tic-Tac-Toe game with Tkinter GUI.

Run the script to play:
  - Click "Start Game" to begin.
  - Alternate turns to place 'X' or 'O'.
  - Game announces the winner or a draw.
  - Click "Retry" to restart.

Author: [Daexion]
"""

from src.gameboard import GameBoard

if __name__ == "__main__":
    game_board = GameBoard()
    game_board.mainloop()
