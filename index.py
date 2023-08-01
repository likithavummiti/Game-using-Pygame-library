import random

class LudoGame:
    def __init__(self):
        self.board = ["-" for _ in range(56)]
        self.players = ["Red", "Green", "Yellow", "Blue"]
        self.player_positions = {
            "Red": -1,
            "Green": -1,
            "Yellow": -1,
            "Blue": -1,
        }
        self.winner = None

    def display_board(self):
        print("-------------------------------")
        for i in range(0, 56, 14):
            row = self.board[i:i+14]
            print(" | ".join(row))
            print("-------------------------------")

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        current_position = self.player_positions[player]
        if current_position == -1 and steps == 6:
            self.player_positions[player] = 0
            self.board[0] = player[0]
        elif current_position != -1:
            new_position = current_position + steps
            if new_position <= 51:
                self.board[current_position] = "-"
                self.player_positions[player] = new_position
                self.board[new_position] = player[0]
            elif current_position + steps == 56:
                self.player_positions[player] = 56
                self.board[current_position] = "-"
                self.winner = player
                print(f"{self.winner} is the winner!")

    def play(self):
        print("Welcome to Ludo Game!")
        while not self.winner:
            for player in self.players:
                if not self.winner:
                    input(f"{player}'s turn: Press Enter to roll the dice.")
                    steps = self.roll_dice()
                    print(f"{player} rolled a {steps}.")
                    self.move_player(player, steps)
                    self.display_board()

if __name__ == "__main__":
    ludo_game = LudoGame()
    ludo_game.play()



