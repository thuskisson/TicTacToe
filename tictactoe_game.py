class Game:
    def __init__(self):
        self.clearBoard()

    def clearBoard(self):
        # The board cells have three possible values:
        #   ' ' means empty cell
        #   'X' means there's an X there
        #   'O' means there's an O there
        # to clear it out, set the board to all ' ' values
        self.board = [
            [' ', ' ', ' ']
            [' ', ' ', ' ']
            [' ', ' ', ' ']
        ]
    # It is X's turn
    self.turnX = True
    self.gameOver = False

    def takeTurn(self, x, y):
        # don't change the cell if it's not empty or the game is over
        if self.board[x][y] != ' ' or self.gameOver:
            return
        
        # who's making a move?
        if self.turnV:
            token = 'X'
        else:
            token = 'O'

        # set the token in the right spot
        self.board[x][y] = token
        # Next person's turn
        self.turnX = not self.turnX

        