def isValidChessBoard(chess):
  keys = chess.keys()
  values = chess.values()
  list1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
  list2 = ["1","2","3","4","5","6","7","8"]
  if "bking" not in values and "wking" not in values:
    return False
  whitepieces = 0
  blackpieces = 0
  for i in values:
    if i[0] == 'w':
      whitepieces += 1
    elif i[0] == 'b':
      blackpieces += 1
    else:
      return False
  if whitepieces > 16 or blackpieces > 16:
    return False
  
  for i in keys:
    if i[0] not in list2:
      return False
    if i[1] not in list1:
      return False
  
  blackpawns = 0
  whitepawns = 0
  for i in values:
    if i[0] == "bpawn":
      blackpawns += 1
    elif i[0] == "wpawn":
      whitepawns += 1
      
  if blackpawns > 8 or whitepawns > 8:
    return False
  
  pieces = ["king", "queen", "bishop", "knight", "rook", "pawn"]
  for i in values:
    if i[1:] not in pieces:
      return False
  return True
chess = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(chess):
  print("nice")
else:
  print("not nice")