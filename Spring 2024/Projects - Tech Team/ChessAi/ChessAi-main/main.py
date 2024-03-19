import keras
import tensorflow as tf
import numpy as np
import chess

model = keras.models.load_model('Chess1.h5')
def compressedBitMap(fen):
  board = chess.Board(fen)
  orderMapping = {
    'k': 0,
    'K': 0,
    'q': 1,
    'Q': 1,
    'r': 2,
    'R': 2,
    'n': 3,
    'N': 3,
    'b': 4,
    'B': 4,
    'p': 5,
    'P': 5
  }
  material = {
    'k': 0,
    'K': 0,
    'q': -9,
    'Q': 9,
    'r': -5,
    'R': 5,
    'n': -3,
    'N': 3,
    'b': -3,
    'B': 3,
    'p': -1,
    'P': 1
  }
  alphabet = 'abcdefgh'
  bitMap = np.zeros((8, 8, 8))
  positions, turn, castlingRights, enPeasant, half1, half2 = fen.split(' ')
  row, column = [0, 0]
  whiteMaterial, blackMaterial = 0, 0
  for letter in positions:
    if letter.isnumeric():
      column += int(letter)
    elif letter == '/':
      row += 1
      column = 0
    else:
      peiceIndex = orderMapping[letter]
      if letter.isupper():
        bitMap[peiceIndex, row, column] = 1
      else:
        bitMap[peiceIndex, row, column] = -1
      if letter.isupper():
        whiteMaterial += material[letter]
      else:
        blackMaterial += material[letter]
      column += 1

  #showing the model the possible squares we can move to, which is known to help the model a lot
  first, second = 6, 7
  if not board.turn:
    first, second = 7, 6

  for move in board.legal_moves:
    column = alphabet.index(str(move)[2])
    row = int(str(move)[3]) - 1
    bitMap[first, row, column] = 1
  board.turn = not board.turn #looking at the possible moves for the person whos turn its not

  for move in board.legal_moves:
    column = alphabet.index(str(move)[2])
    row = int(str(move)[3]) - 1
    bitMap[second, row, column] = 1
  #since we originally placed the pieces by defining rank 0 as the eigth index, we have to flip this list to stay in accordance to the definition
  bitMap[6] = bitMap[6][::-1]
  bitMap[7] = bitMap[7][::-1]
  return bitMap

def eval(fen):
  x = np.array(compressedBitMap(fen)[0])
  x = np.reshape(x, (1, 1, 8, 8, 8))
  prediction = model.predict(x, verbose = False)
  return prediction

def minMax(board, depth = 3, maximizingPlayer=True): #should return the best move according to the model
  _ = 0
  if depth == 0:
    return eval(board.fen()), -1
  elif board.outcome() != None:
    if board.is_checkmate():
      if board.turn: #whites move
        return -1000, _ #since white can't do anything
      return 1000, _
    else:
      return 0, _

  if maximizingPlayer:
    value = float('inf') * -1
    legal = list(board.legal_moves)
    bestMove = legal[0]
    for move in board.legal_moves:
      newBoard = board.copy()
      newBoard.push(move)
      result = minMax(newBoard, depth-1, maximizingPlayer=False)[0]
      if result > value:
        value = result
        bestMove = move
  else:
    value = float('inf')
    legal = list(board.legal_moves)
    bestMove = legal[0]
    for move in board.legal_moves:
      newBoard = board.copy()
      newBoard.push(move)
      result = minMax(newBoard, depth-1, maximizingPlayer=True)[0]
      if result < value:
        value = result
        bestMove = move
  return value, bestMove

def main(board, isWhitesMove = True):
  return minMax(board, depth=3, maximizingPlayer=isWhitesMove)[1]