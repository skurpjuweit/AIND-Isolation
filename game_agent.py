"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    return custom_score_6(game, player)

def custom_score_2(game, player):
    """Heuristic: Maximize the distance from the other player

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    y1, x1 = game.get_player_location(player)
    y2, x2 = game.get_player_location(game.get_opponent(player))
    return float((y1 - y2)**2 + (x1 - x2)**2)

def custom_score_3(game, player):
    """Heuristic: Maximize the distance from the other player, but minimize distance to the center of the board.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y1, x1 = game.get_player_location(player)
    y2, x2 = game.get_player_location(game.get_opponent(player))
    return float((y1 - y2)**2 + (x1 - x2)**2) - float((h - y1)**2 + (w - x1)**2)

def custom_score_4(game, player):
    """Heuristic: Minimize the distance to the blank fields

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    blanks = game.get_blank_spaces()

    a, b = game.get_player_location(player)
    sum_dist = 0
    for blank in blanks:
        x, y = blank
        dist_blank = float((a - x)**2 + (b - y)**2)
        sum_dist += dist_blank

    return float(-sum_dist)

def custom_score_5(game, player):
    """Heuristic: Maximize the open moves available after the next move

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    legal_moves = game.get_legal_moves(player)
    v = 0
    for m in legal_moves:
        v += get_open_moves_count(game, m)

    return float(v)

def custom_score_6(game, player):
    """Heursitic: aximize the open moves available after the next move, but balance it against the moves 
    available to the opponent after the next move.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    legal_moves = game.get_legal_moves(player)
    v = 0
    for m in legal_moves:
        v += get_open_moves_count(game, m)

    legal_moves = game.get_legal_moves(game.get_opponent(player))
    w = 0
    for m in legal_moves:
        w += get_open_moves_count(game, m)

    return float(v - w)

def custom_score_7(game, player):
    """Heursitic: Maximize the open moves available after the next move, but balance it against the moves 
    available to the opponent after the next move. Also consider, that the opponent could move onto one of the field in the next move.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    legal_moves_1 = game.get_legal_moves(player)
    legal_moves_2 = game.get_legal_moves(game.get_opponent(player))

    overlap = set(legal_moves_1).intersection(legal_moves_2)

    v = 0
    for m in legal_moves_1:
        if m not in overlap:
            v += get_open_moves_count(game, m)

    w = 0
    for m in legal_moves_2:
        if m not in overlap:
            w += get_open_moves_count(game, m)

    return float(v - w)

def get_open_moves_count(game, loc):
    """
    """
    r, c = loc

    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
    valid_moves = [(r + dr, c + dc) for dr, dc in directions
                  if game.move_is_legal((r + dr, c + dc))]

    return len(valid_moves)

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def max_value(self, game, depth):
        """Helper method to Implement recursive depth-limited minimax search algorithm as described in
        the lectures.

        **********************************************************************
            Will be called by method minimax, no need to call directly
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        utility_value: float
            utility value of the situation represented by the board encoded in the parameter game.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return(self.score(game, self))
        v = float("-inf")

        for cand_m   in game.get_legal_moves(self):
            cand_game = game.forecast_move(cand_m)
            cand_v = self.min_value(cand_game, depth - 1)
            if cand_v > v:
                v = cand_v
        return v

    def min_value(self, game, depth):
        """Helper method to Implement recursive depth-limited minimax search algorithm as described in
        the lectures.

        **********************************************************************
            Will be called by method minimax, no need to call directly
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        utility_value: float
            utility value of the situation represented by the board encoded in the parameter game.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return(self.score(game, self))
        v = float("+inf")

        for cand_m in game.get_legal_moves(game.get_opponent(self)):
            cand_game = game.forecast_move(cand_m)
            cand_v = self.max_value(cand_game, depth - 1)
            if cand_v < v:
                v = cand_v
        return v


    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        v = float("-inf")
        m = (-1. - 1)

        for cand_m in game.get_legal_moves(self):
            cand_game = game.forecast_move(cand_m)
            cand_v = self.min_value(cand_game, depth - 1)
            if cand_v > v:
                v = cand_v
                m = cand_m

        return m

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def max_value(self, game, depth, alpha, beta):
        """Helper method to Implement recursive depth-limited minimax search algorithm as described in
        the lectures.

        **********************************************************************
            Will be called by method minimax, no need to call directly
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        utility_value: float
            utility value of the situation represented by the board encoded in the parameter game.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1,-1)

        if game.is_winner(self) or game.is_loser(self):
            return self.score(game, self), (-1,-1)

        v = float("-inf")
        m = (-1. -1)

        for cand_m in game.get_legal_moves(self):
            cand_game = game.forecast_move(cand_m)
            cand_v, _ = self.min_value(cand_game, depth - 1, alpha, beta)
            if cand_v > v:
                v = cand_v
                m = cand_m
            if v >= beta:
                return v, m
            alpha = max(alpha, v)
        return v, m

    def min_value(self, game, depth, alpha, beta):
        """Helper method to Implement recursive depth-limited minimax search algorithm as described in
        the lectures.

        **********************************************************************
            Will be called by method minimax, no need to call directly
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        utility_value: float
            utility value of the situation represented by the board encoded in the parameter game.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self), (-1,-1)

        if game.is_winner(self) or game.is_loser(self):
            return self.score(game, self), (-1,-1)

        v = float("+inf")
        m = (-1, -1)

        for cand_m in game.get_legal_moves(game.get_opponent(self)):
            cand_game = game.forecast_move(cand_m)
            cand_v, _ = self.max_value(cand_game, depth - 1, alpha, beta)
            if cand_v < v:
                v = cand_v
                m = cand_m
            if v <= alpha:
                return v, m
            beta = min(beta, v)
        return v, m

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            d = 0
            while True:
                best_move = self.alphabeta(game, d)
                d += 1

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        v, m = self.max_value(game, depth, alpha, beta)

        return m

