# class that stores details of all the games for score board
class Game:
    name = ''
    complexity = []
    result = []
    num_attempt = []

    def append_player_data(self, complexity, result, num_attempt):
        self.complexity.append(complexity)
        self.result.append(result)
        self.num_attempt.append(num_attempt)
