import random


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                row, col = map(
                    int,
                    input(
                        f"Player {self.symbol}, enter row and column numbers (1, 2, 3) to fix spot: "
                    ).split(),
                )
                if 0 < row < 4 and 0 < col < 4:
                    return row - 1, col - 1
            except ValueError:
                pass
            print("Invalid input. Please enter again!")


class Board:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]

    def is_spot_empty(self, row, col):
        return self.board[row][col] == "-"

    #  fix_spot place the symbol in the board or not, when not it return false because the spot is already taken
    def fix_spot(self, row, col, symbol):
        if self.is_spot_empty(row, col):
            self.board[row][col] = symbol
            return True
        return False

    def is_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or all(
                self.board[j][i] == symbol for j in range(3)
            ):
                return True
        if all(self.board[i][i] == symbol for i in range(3)) or all(
            self.board[i][2 - i] == symbol for i in range(3)
        ):
            return True
        return False

    def is_draw(self):
        return all(cell != "-" for row in self.board for cell in row)

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player = random.choice(self.players)

    def switch_player(self):
        self.current_player = self.players[not self.players.index(self.current_player)]

    def play_game(self):
        while True:
            self.board.display_board()
            row, col = self.current_player.get_move()

            if not self.board.fix_spot(row, col, self.current_player.symbol):
                print("Spot already taken. Try again.")
                continue

            if self.board.is_winner(self.current_player.symbol):
                self.board.display_board()
                print(f"Player {self.current_player.symbol} wins!")
                return

            if self.board.is_draw():
                self.board.display_board()
                print("Match Draw!")
                return

            self.switch_player()


if __name__ == "__main__":
    game = Game()
    game.play_game()
