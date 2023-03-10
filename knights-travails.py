

#class defining a square on the chessboard
class Square:
    #class constructor
    def __init__(self, coord=(), right="", left="", top="", bot=""):
        self.coord = coord
        self.right = right
        self.left = left
        self.top = top
        self.bot = bot

#class defining an nxm chessboard
class Board:
    #class constructor
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.squares = self.constructBoard()
    
    #class method which constructs a chessboard of the input size
    def constructBoard(self):
        squares = []
        for i in range(self.rows):
            for j in range(self.cols):
                square = Square((i,j))
                if (0 < j):
                    square.left = (i, j-1)
                else:
                    square.left = None
                if (j < 3):
                    square.right = (i, j+1)
                else:
                    square.right = None
                if (0 < i):
                    square.top = (i-1, j)
                else:
                    square.top = None
                if (i < 3):
                    square.bot = (i+1, j)
                else:
                    square.bot = None
                squares.append(square)
        return squares
    
#class defining a knight chesspiece
class Knight:
    #class constructor
    def __init__(self, current_pos=[]):
        self.current_pos = current_pos
        self.moves = self.findMoves() #adjacency list for current position

    #class method which finds possible moves based on current position
    def findMoves(self):
        moves = [
            [self.current_pos[0]+1, self.current_pos[1]+2],
            [self.current_pos[0]+2, self.current_pos[1]+1],
            [self.current_pos[0]-2, self.current_pos[1]-1],
            [self.current_pos[0]-1, self.current_pos[1]-2],
            [self.current_pos[0]-1, self.current_pos[1]+2],
            [self.current_pos[0]-2, self.current_pos[1]+1],
            [self.current_pos[0]+2, self.current_pos[1]-1],
            [self.current_pos[0]+1, self.current_pos[1]-2],
        ]
        return moves


def knightMoves(knight, target, board, prevPath):
    # path =  kwargs.get('path', [knight.current_pos])
    path = prevPath
    print(knight.current_pos, path)
    #if target is off the board, return false
    if not any(square.coord == target for square in board):
        print('target not on the board')
        return False
    if not any(square.coord == knight.current_pos for square in board):
        print('potential move not on the board')
        return False
    if (knight.current_pos == target):
        return target
    else: 
        #move
        for move in knight.moves:
            nextKnight = Knight(knight.current_pos)
            path.append(knightMoves(nextKnight, target, board, path))
    return path


#define 8x8 board of squares
board = Board(8,8)

# for square in board.squares:
#     print (square.coord)
# print (board.squares[1].coord, board.squares[1].right, board.squares[1].left, board.squares[1].top, board.squares[1].bot)

knight = Knight([4,4])
# print(knight.current_pos)
# print(knight.moves)

print(knightMoves(knight, (7,7), board.squares, [knight.current_pos]))






