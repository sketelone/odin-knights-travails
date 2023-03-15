
#class defining a square on the chessboard
class Square:
    #class constructor
    def __init__(self, coord=[]):
        self.coord = coord

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
                square = Square([i,j])
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

#class defining a node
class Node:
    #class constructor
    def __init__(self, value = None, parent = None, leaves = []):
        self.value = value
        self.parent = parent
        self.leaves = leaves

def knightMoves(knight, target, board):
    #if target is off the board, return false
    if not any(square.coord == target for square in board):
        print('target not on the board')
        return False
    else: 
        #build tree of shortest path to each tile starting from current position
        root = constructTree(knight, board)
        print(root.value, len(root.leaves))
        #find path to target
        path = findPath(root, target)
    return path

#returns an array of all nodes in the tree
def preorder (node, array):
    array.append(node.value)
    for leaf in node.leaves:
        preorder(leaf, array)
    return array

#finds the target node in the graph and returns an array of path from root to target
def findPath(root, target):
    #initalize variables
    path = []   #path of nodes from root to target
    queue = []  #queue of nodes to be visited

    #initalize node as root
    node = root
    #while current node is not target
    while not node.value == target:
        #add all leaves to queue
        for leaf in node.leaves:
            queue.append(leaf)
        #move to next node in queue
        node = queue[0]
        queue.remove(queue[0])
    #once target is found, add it to path
    path.append(target)
    #while current node is not root, add parent to path and move to parent
    while not node.parent == None:
        path.append(node.parent.value)
        node = node.parent
    #reverse path to be in root --> target order
    path.reverse()
    return path

#constructs a graph of all shortest routes to all other squares on the board from starting square
def constructTree(knight, board):

    #initialize variables
    n = len(board)  #total number of nodes
    n_nodes = 1     #current number of nodes
    treeArray = [knight.current_pos] #array of nodes in tree
    queue = []      #queue of nodes to visit

    #define the root as the starting position
    root = Node(knight.current_pos)
    #initialize node at root
    node = root

    #while all nodes have not been added to the tree
    while not n_nodes == n:
        #for all possible moves
        for move in knight.moves:
            #if move is on the board, not already in the tree and not already in the queue, 
            # add it to the tree array, create a new node and add it to the tree, and increment num of nodes
            if any(square.coord == move for square in board) and move not in treeArray and not any(item.value == move for item in queue):
                treeArray.append(move)
                node.leaves.append(Node(move, node, []))
                n_nodes += 1
        #add all nodes to the queue
        for leaf in node.leaves:
            queue.append(leaf)
        #move to the next node in the queue
        node = queue[0]
        knight = Knight(queue[0].value)
        queue.remove(queue[0])
    return root

#define 8x8 board of squares
board = Board(8,8)

#define knight with starting position
knight = Knight([0,0])

print(knightMoves(knight, [7,7], board.squares))




