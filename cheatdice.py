import random

class MulliganCheater:
    def __init__(self):
        self.mulligan_used = False
    
    def roll_dice(self):
        if not self.mulligan_used:
            dice_sum = 0
            for _ in range(3):
                dice_sum += random.randint(1, 6)
            if dice_sum < 9:
                self.mulligan_used = True
                return self.roll_dice()
            else:
                return dice_sum
        else:
            return random.randint(3, 18)

class DiceGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
    
    def play_round(self):
        player1_roll = self.player1.roll_dice()
        player2_roll = self.player2.roll_dice()
        if player1_roll > player2_roll:
            self.player1_score += 1
            print("Player 1 wins the round!")
        elif player2_roll > player1_roll:
            self.player2_score += 1
            print("Player 2 wins the round!")
        else:
            print("It's a tie!")
    
    def play_game(self, num_rounds):
        for i in range(num_rounds):
            print(f"Round {i+1}:")
            self.play_round()
            print(f"Score: Player 1 {self.player1_score}, Player 2 {self.player2_score}")
    
    def get_winner(self):
        if self.player1_score > self.player2_score:
            return "Player 1"
        elif self.player2_score > self.player1_score:
            return "Player 2"
        else:
            return "It's a tie!"

# Example usage
player1 = MulliganCheater()
player2 = MulliganCheater()
game = DiceGame(player1, player2)
game.play_game(5)
print("Final score:", game.get_winner())
