import time
from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)
from reversi import from_dictionary_to_array_board


class Solution1(StudentHeuristic):
  def get_name(self) -> str:
    return "Paprika"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    # We get the board of the state in a list
    board = from_dictionary_to_array_board(state.board, 8, 8)

    # We get the label of our player and enemy
    if (state.is_player_max(state.next_player)):
      me = state.next_player.label
      enemy = state.previous_player.label
    else:
      me = state.previous_player.label
      enemy = state.next_player.label

    # We store the strategic positions of the board that the heuristic will take into account
    corners = ((0,0), (0,7), (7,0), (7,7))
    xcells = ((1,1), (1,6), (6,1), (6,6))
    ccells = ((0,1), (1,0), (1,7), (0,6), (7,1), (6,0), (7,6), (6,7))

    val = 100

    # The c and x cells are a bad move so we penalize them
    for cell in ccells:
      if (board[cell[0]][cell[1]] == me):
        val -= 4
      elif (board[cell[0]][cell[1]] == enemy):
        val += 4

    for cell in xcells:
      if (board[cell[0]][cell[1]] == me):
        val -= 10
      elif (board[cell[0]][cell[1]] == enemy):
        val += 10

    # The corners are a great move so we favour them
    for cell in corners:
      if (board[cell[0]][cell[1]] == me):
        val += 20
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 20

    return val


class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "Peppermint"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    # We get the board of the state in a list
    board = from_dictionary_to_array_board(state.board, 8, 8)

    # We get the label of our player and enemy
    if (state.is_player_max(state.next_player)):
      me = state.next_player.label
      enemy = state.previous_player.label
    else:
      me = state.previous_player.label
      enemy = state.next_player.label

    # We store the strategic positions of the board that the heuristic will take into account
    corners = ((0,0), (0,7), (7,0), (7,7))
    xcells = ((1,1), (1,6), (6,1), (6,6))
    scells = ((2,2), (5,5), (2,5), (5,2))
    ccells = ((0,1), (1,0), (1,7), (0,6), (7,1), (6,0), (7,6), (6,7))
    acells = ((0,2), (2,0), (0,5), (5,0), (7,2), (2,7), (7,5), (5,7))
    bcells = ((0,3), (3,0), (0,4), (4,0), (7,3), (3,7), (7,4), (4,7))
    dcells = ((2,3), (3,2), (2,4), (4,2), (5,3), (3,5), (5,4), (4,5))
    ecells = ((1,2), (1,5), (6,2), (6,5), (2,1), (2,6), (5,1), (5,6))
    fcells = ((1,3), (1,4), (6,3), (6,4), (3,1), (3,6), (4,1), (4,6))

    val = 784

    # The corners are a great move so we favour them    
    for cell in corners:
      if (board[cell[0]][cell[1]] == me):
        val += 99
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 99

    for cell in xcells:
      if (board[cell[0]][cell[1]] == me):
        val += -24
      elif (board[cell[0]][cell[1]] == enemy):
        val -= -24

    for cell in scells:
      if (board[cell[0]][cell[1]] == me):
        val += 7
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 7

    for cell in ccells:
      if (board[cell[0]][cell[1]] == me):
        val += -8
      elif (board[cell[0]][cell[1]] == enemy):
        val -= -8

    for cell in acells:
      if (board[cell[0]][cell[1]] == me):
        val += 8
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 8

    for cell in bcells:
      if (board[cell[0]][cell[1]] == me):
        val += 6
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 6

    for cell in dcells:
      if (board[cell[0]][cell[1]] == me):
        val += 4
      elif (board[cell[0]][cell[1]] == enemy):
        val -= 4

    for cell in ecells:
      if (board[cell[0]][cell[1]] == me):
        val += -4
      elif (board[cell[0]][cell[1]] == enemy):
        val -= -4

    for cell in fcells:
      if (board[cell[0]][cell[1]] == me):
        val += -3
      elif (board[cell[0]][cell[1]] == enemy):
        val -= -3

    return val


class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "Cinnamon"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    # We get the label of our player and enemy
    if (state.is_player_max(state.next_player)):
      me = state.next_player.label
      enemy = state.previous_player.label
    else:
      me = state.previous_player.label
      enemy = state.next_player.label

    # We call peppermint
    peppermint = Solution2()
    val = peppermint.evaluation_function(state)
    
    val += len(state.game._get_valid_moves(state.board, me))*10

    return val