import time
from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)

class SolutionTicTacToe(StudentHeuristic):

  def get_name(self) -> str:
    return "3 en Raxa"

  def evaluation_function(self, state: TwoPlayerGameState) -> float:
    # let's use an auxiliary function
    ret = self.detectEnemyLine(state.board, state.next_player.label)
    return ret

  def detectEnemyLine(self, board, enemy) -> int:
    if(enemy == -1):
      me = 1
    else:
      me = -1

    ret = 0

    # Check horizontal lines.
    ret += self.evaluateLine((board[0][0], board[1][0], board[2][0]), me, enemy)
    ret += self.evaluateLine((board[0][1], board[1][1], board[2][1]), me, enemy)
    ret += self.evaluateLine((board[0][2], board[1][2], board[2][2]), me, enemy)

    # Check vertical lines.
    ret += self.evaluateLine((board[0][0], board[0][1], board[0][2]), me, enemy)
    ret += self.evaluateLine((board[1][0], board[1][1], board[1][2]), me, enemy)
    ret += self.evaluateLine((board[2][0], board[2][1], board[2][2]), me, enemy)

    # Check diagonal lines
    ret += self.evaluateLine((board[0][0], board[1][1], board[2][2]), me, enemy)
    ret += self.evaluateLine((board[0][2], board[1][1], board[2][0]), me, enemy)

    return ret

  def evaluateLine(self, line, me, enemy):
    cMe = 0
    cEnemy = 0

    for cell in line:
      if(cell == enemy):
        cEnemy += 1
      elif(cell == me):
        cMe += 1

    if(cMe == 3):
      return -1000
    if(cEnemy == 3):
      return 500
    if(cEnemy == 2 and cMe == 0):
      return 50
    if(cEnemy == 0 and cMe == 2):
      return -50
    if(cEnemy == 0 and cMe == 1):
      return -25
    if(cEnemy == 0 and cMe == 1):
      return 25
    return 0