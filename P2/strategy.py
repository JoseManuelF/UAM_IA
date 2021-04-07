"""Strategies for two player games.

   Authors:
        Fabiano Baroni <fabiano.baroni@uam.es>,
        Alejandro Bellogin <alejandro.bellogin@uam.es>
        Alberto Suárez <alberto.suarez@uam.es>
"""

from __future__ import annotations  # For Python 3.7

from abc import ABC, abstractmethod
from typing import List

import numpy as np

from game import TwoPlayerGame, TwoPlayerGameState
from heuristic import Heuristic


class Strategy(ABC):
    """Abstract base class for player's strategy."""

    def __init__(self, verbose: int = 0) -> None:
        """Initialize common attributes for all derived classes."""
        self.verbose = verbose

    @abstractmethod
    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""

    def generate_successors(
        self,
        state: TwoPlayerGameState,
    ) -> List[TwoPlayerGameState]:
        """Generate state successors."""
        assert isinstance(state.game, TwoPlayerGame)
        successors = state.game.generate_successors(state)
        assert successors  # Error if list is empty
        return successors


class RandomStrategy(Strategy):
    """Strategy in which moves are selected uniformly at random."""

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""
        successors = self.generate_successors(state)
        return np.random.choice(successors)


class ManualStrategy(Strategy):
    """Strategy in which the player inputs a move."""

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next move."""
        successors = self.generate_successors(state)

        assert isinstance(state.game, TwoPlayerGame)
        if gui:
            index_successor = state.game.graphical_input(state, successors)
        else:
            index_successor = state.game.manual_input(successors)

        next_state = successors[index_successor]

        if self.verbose > 0:
            print('My move is: {:s}'.format(str(next_state.move_code)))

        return next_state


class MinimaxStrategy(Strategy):
    """Minimax strategy."""

    def __init__(
        self,
        heuristic: Heuristic,
        max_depth_minimax: int,
        verbose: int = 0,
    ) -> None:
        """Initialize depth of the search & heuristic."""
        super().__init__(verbose)
        self.heuristic = heuristic
        self.max_depth_minimax = max_depth_minimax

    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next state in the game."""

        successors = self.generate_successors(state)

        minimax_value = -np.inf

        for successor in successors:
            if self.verbose > 1:
                print('{}: {}'.format(state.board, minimax_value))

            successor_minimax_value = self._min_value(
                successor,
                self.max_depth_minimax,
            )
            if (successor_minimax_value > minimax_value):
                minimax_value = successor_minimax_value
                next_state = successor

        if self.verbose > 0:
            if self.verbose > 1:
                print('\nGame state before move:\n')
                print(state.board)
                print()
            print('Minimax value = {:.2g}'.format(minimax_value))

        return next_state

    def _min_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
    ) -> float:
        """Min step of the minimax algorithm."""
        if state.end_of_game or depth == 0:
            minimax_value = self.heuristic.evaluate(state)

        else:
            minimax_value = np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, minimax_value))

                successor_minimax_value = self._max_value(
                    successor, depth - 1,
                )
                if (successor_minimax_value < minimax_value):
                    minimax_value = successor_minimax_value

        if self.verbose > 1:
            print('{}: {}'.format(state.board, minimax_value))

        return minimax_value

    def _max_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
    ) -> float:
        """Max step of the minimax algorithm."""
        if state.end_of_game or depth == 0:
            minimax_value = self.heuristic.evaluate(state)

        else:
            minimax_value = -np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, minimax_value))

                successor_minimax_value = self._min_value(
                    successor, depth - 1,
                )
                if (successor_minimax_value > minimax_value):
                    minimax_value = successor_minimax_value

        if self.verbose > 1:
            print('{}: {}'.format(state.board, minimax_value))

        return minimax_value


class MinimaxAlphaBetaStrategy(Strategy):
    """Minimax alpha-beta strategy."""

    def __init__(
        self,
        heuristic: Heuristic,
        max_depth_minimax: int,
        verbose: int = 0,
    ) -> None:
        super().__init__(verbose)
        self.heuristic = heuristic
        self.max_depth_minimax = max_depth_minimax


    def next_move(
        self,
        state: TwoPlayerGameState,
        gui: bool = False,
    ) -> TwoPlayerGameState:
        """Compute next state in the game."""

        # We get the successors of the state given
        successors = self.generate_successors(state)

        # We set the minimum value possible for alpha and the maximum for beta
        alpha = -np.inf
        beta = np.inf

        # For each successor of the root state
        for successor in successors:
            if self.verbose > 1:
                print('{}: [{},{}]'.format(state.board, alpha, beta))

            min_value = self._min_value(
                successor,
                self.max_depth_minimax,
                alpha,
                beta,
            )

            # We get the maximum value possible for alpha
            if (min_value > alpha):
                alpha = min_value
                next_state = successor

        if self.verbose > 0:
            if self.verbose > 1:
                print('\nGame state before move:\n')
                print(state.board)
                print()
            print('Alpha value = {:.2g}'.format(alpha))

        return next_state


    def _max_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
        alpha: int,
        beta: int,
    ) -> float:

        # We reached the maximum depth or the last state
        if state.end_of_game or depth == 0:
            max_value = self.heuristic.evaluate(state)

        else:
            max_value = -np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, max_value))

                min_value = self._min_value(
                    successor, depth - 1, alpha, beta,
                )

                # We get the maximum value possible among all the successors
                if (min_value > max_value):
                    max_value = min_value

                # We want alpha to be the highest value possible
                if (max_value > alpha):
                    alpha = max_value

                # In case of beta being lower or equal than alpha
                # we can prune the rest of the successors
                if (beta <= alpha):
                    break

        if self.verbose > 1:
            print('{}: {}'.format(state.board, max_value))

        return max_value


    def _min_value(
        self,
        state: TwoPlayerGameState,
        depth: int,
        alpha: int,
        beta: int,
    ) -> float:
    
        # We reached the maximum depth or the last state
        if state.end_of_game or depth == 0:
            min_value = self.heuristic.evaluate(state)

        else:
            min_value = np.inf

            successors = self.generate_successors(state)
            for successor in successors:
                if self.verbose > 1:
                    print('{}: {}'.format(state.board, min_value))

                max_value = self._max_value(
                    successor, depth - 1, alpha, beta,
                )

                # We get the minimum value possible among all the successors
                if (max_value < min_value):
                    min_value = max_value

                # We want beta to be the lowest value possible
                if (min_value < beta):
                    beta = min_value

                # In case of beta being lower or equal than alpha
                # we can prune the rest of the successors
                if (beta <= alpha):
                    break

        if self.verbose > 1:
            print('{}: {}'.format(state.board, min_value))

        return min_value
