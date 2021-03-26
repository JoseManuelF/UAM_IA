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
    return "Salt"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    enemy = state.next_player.label
    board = from_dictionary_to_array_board(state.board, 8, 8)

    if(enemy == -1):
      me = 1
    else:
      me = -1

    val = 64
    for line in board:
      for cell in line:
        if(cell == me):
          val -= 1
        elif(cell == enemy):
          val += 1

    return val

class Solution2(StudentHeuristic):
  def get_name(self) -> str:
    return "Pepper"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    enemy = state.next_player.label
    board = from_dictionary_to_array_board(state.board, 8, 8)

    if(enemy == -1):
      me = 1
    else:
      me = -1

    val = 112
    for x in range(8):
      for y in range(8):
        if(board[x][y] == me and (x == 0 or x == 7) and (y == 0 or y == 7)):
          val -= 16
        elif(board[x][y] == me and (x == 0 or x == 7) or (y == 0 or y == 7)):
          val -= 2

    return val

class Solution3(StudentHeuristic):
  def get_name(self) -> str:
    return "Salt&Pepper"
    
  def evaluation_function(self, state: TwoPlayerGameState) -> float:

    sol1 = Solution1
    sol2 = Solution2

    #More importance to Solution1, as we consider it a better approach
    val = sol1.evaluation_function(sol1, state)*2
    val += sol2.evaluation_function(sol2, state)

    return val