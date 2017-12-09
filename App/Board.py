from random import choice
from Exception.AlreadyEndedGameException import AlreadyEndedGameException


class Board:
    winner_player = 'Player'
    winner_cpu = 'CPU'
    tie = 'Tie'

    def __init__(self, dimension):
        self.winner = self.tie
        self.dimension = dimension
        self.matrix = []
        self.positions = []

        self.generate(dimension)

    def generate(self, dimension):
        self.matrix = [[_ for _ in xrange(dimension)] for _ in xrange(dimension)]

        for i in range(0, dimension):
            for j in range(0, dimension):
                self.matrix[i][j] = '_'
                self.positions.append(str(i + 1) + str(j + 1))

    def paint(self):
        for i in range(0, self.dimension):
            print(self.matrix[i])

    def player_position(self, position):
        self.set_position(position, 'X')

    def random_position(self):
        self.set_position(choice(self.positions), 'O')

    def set_position(self, position, value):
        try:
            self.positions.index(position)
        except ValueError:
            raise ValueError

        self.matrix[int(position[:1]) - 1][int(position[1:]) - 1] = value
        self.positions.remove(position)

        if self.is_ended():
            raise AlreadyEndedGameException('Hello there')

    def get_winner(self):
        return self.winner

    def is_a_tie(self):
        return self.winner == self.tie

    def is_a_player_win(self):
        return self.winner == self.winner_player

    def is_a_cpu_win(self):
        return self.winner == self.winner_cpu

    def is_ended(self):

        for i in range(0, self.dimension):
            if self.check_col(i, 'X') or self.check_row(i, 'X') or self.check_left_dg('X') or self.check_right_dg('X'):
                self.winner = self.winner_player
                break
            if self.check_col(i, 'O') or self.check_row(i, 'O') or self.check_left_dg('O') or self.check_right_dg('O'):
                self.winner = self.winner_cpu
                break

        return len(self.positions) == 0 or self.winner != self.tie

    def check_col(self, column, value):
        for i in range(0, self.dimension):
            if self.matrix[i][column] != value:
                return False

        return True

    def check_row(self, row, value):
        for i in range(0, self.dimension):
            if self.matrix[row][i] != value:
                return False

        return True

    def check_left_dg(self, value):
        for i in range(0, self.dimension):
            if self.matrix[i][i] != value:
                return False

        return True

    def check_right_dg(self, value):
        for i in range(0, self.dimension):
            if self.matrix[i][self.dimension - i - 1] != value:
                return False

        return True
