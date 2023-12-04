class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1

    def get_score_name(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return scores[self.score]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.won_point()
        elif player_name == self.player2.name:
            self.player2.won_point()

    def get_score(self):
        if self.player1.score == self.player2.score:
            if self.player1.score < 3:
                return f"{self.player1.get_score_name()}-All"
            else:
                return "Deuce"
        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.advantage_win() if abs(self.player1.score - self.player2.score) < 2 else self.advantage_win()
        else:
            return self.score()

    def tie(self):
        if self.player1.score < 3:
            return f"{self.player1.get_score_name()}-All"
        else:
            return "Deuce"

    def advantage_win(self):
        minus_result = self.player1.score - self.player2.score
        if minus_result == 1:
            return f"Advantage {self.player1.name}"
        elif minus_result == -1:
            return f"Advantage {self.player2.name}"
        elif minus_result >= 2:
            return f"Win for {self.player1.name}"
        else:
            return f"Win for {self.player2.name}"

    def score(self):
        return f"{self.player1.get_score_name()}-{self.player2.get_score_name()}"
