# https://fivethirtyeight.com/features/can-you-track-the-delirious-ducks/

import random


class Grid:
    """
    3 x 3 rock grid
    """
    MIN, MAX = 0, 2  # min and max for both x and y coordinates in the grid

    def __init__(self):
        self.moves = {}
        for x in range(self.MIN, self.MAX + 1):
            for y in range(self.MIN, self.MAX + 1):
                coords = (x, y)
                self.moves[coords] = self.possible_moves(coords)

    def possible_moves(self, coords):
        """
        return a list containing each move = tuple(delta_x, delta_y) which is legal from the given coords
        :param coords: tuple(x, y)
        :return:
        """
        moves = []
        if coords[0] > self.MIN:
            moves.append((-1, 0))
        if coords[0] < self.MAX:
            moves.append((+1, 0))
        if coords[1] > self.MIN:
            moves.append((0, -1))
        if coords[1] < self.MAX:
            moves.append((0, +1))
        return moves

    def play_round(self, ducks_coords, show=False):
        """
        have each duck make a random legal move from its starting position
        :param ducks_coords: list of initial coordinate tuples, one for each duck
        :param show: if True, then print the new coordinates
        :return: list of new coordinate tuples
        """
        new_ducks_coords = []
        for duck_coords in ducks_coords:
            move = random.choice(self.moves[duck_coords])
            new_coords = (duck_coords[0] + move[0], duck_coords[1] + move[1])
            new_ducks_coords.append(new_coords)
        if show: print(new_ducks_coords)
        return new_ducks_coords

    def play_game(self, ducks_coords, show=False):
        """
        have each duck make random legal moves till all ducks are all at the same coordinates,
        after making at least one move
        :param ducks_coords: list of initial coordinate tuples, one for each duck
        :param show: if True, then print the new coordinates after each move
        :return: the count of moves taken
        """
        ducks_coords = self.play_round(ducks_coords, show)
        count = 1
        while any([coords != ducks_coords[0] for coords in ducks_coords[1:]]):
            ducks_coords = self.play_round(ducks_coords, show)
            count += 1
        return count

    def expected_moves(self, ducks_coords, n_games=1000000):
        """
        compute the expected number of moves for all ducks to be at the same coordinates,
        after making at least one move
        :param ducks_coords: list of initial coordinate tuples, one for each duck
        :param n_games: nr. of tries to simulate
        :return: expected value
        """
        total = 0
        for _ in range(n_games):
            total += self.play_game(ducks_coords)
        return total / n_games


grid = Grid()
initial_coords = (1, 1)
for n_ducks in range(2, 4):
    ducks_initial_coords = [initial_coords] * n_ducks
    print('Expected number of moves with %d ducks = %.3f' % (n_ducks, grid.expected_moves(ducks_initial_coords)))
