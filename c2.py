#Given a chessboard with one K and one Q, see if the K can attack the Q.
#This function is given coordinates for the king and queen on a chessboard.
#These coordinates are given as a letter A-H for the columns and 1-8 for the row, like "D6" and "B7":

def check(king, queen):
    #Convert the letters coordinates
    king_col = ord(king[0]) - ord('A') + 1
    king_row = int(king[1])
    
    queen_col = ord(queen[0]) - ord('A') + 1
    queen_row = int(queen[1])
    
    #Check if the king is in a position to attack the queen
    if abs(king_col - queen_col) <= 1 and abs(king_row - queen_row) <= 1:
        return True
    return False

#Example
print(check("D6", "E7"))  # True, king can attack
print(check("D6", "C5"))  # True, king can attack
print(check("D6", "C7"))  # False, king cannot attack
