from Board import Board
from Exception.AlreadyEndedGameException import AlreadyEndedGameException
import time


class Game:
    def __init__(self, dimension):
        self.board = Board(dimension)
        self.board.random_position()

    def play(self):
        while not self.board.is_ended():
            self.board.paint()

            try:
                position = raw_input('\nSelect a position: ')
                self.board.player_position(position)
                self.board.random_position()

            except AlreadyEndedGameException:
                break
            except ValueError:
                print('\nOps! Non-existent or occupied position. Try it again, please.')

        self.board.paint()

        if self.board.is_a_player_win():
            print('\nCongratulations! You win!')
        elif self.board.is_a_cpu_win():
            print('\nOoops! You lose. Smile, robots are meant to rule the world.')
        else:
            print('\nResult: TIE')

        time.sleep(3)
