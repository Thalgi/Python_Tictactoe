class User :

    def __init__(self,marker):
        self.marker = marker

    def get_move(self):
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for Player {self.marker}: "))
                col = int(input(f"Enter column (0, 1, or 2) for Player {self.marker}: "))

                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

