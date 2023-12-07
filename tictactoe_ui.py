import sys
import math
import random
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from tictactoe_game import Game

class WinnerDialog(QDialog):
    def __init__(self, winner):
        super().__init__()

        self.setWindowTitle(winner + ' has won!')

        # OK button to play again, cancel button to not play again
        qbtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(qbtn)
        # These are built into the dialog, and we'll check for OK
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # show the dialog
        self.layout = QVBoxLayout()
        lbl = QLabel("Congratulations " + winner + ". New Game?")
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        #Initially start off with a nice square window
        self.resize(500, 500)
        self.setWindowTitle("Tic-Tac-Toe")

        # commented out for now since we haven't made it yet
        self.game = Game()

    # respond to paint events
    def paintEvent(self, event):
        qp = QPainter(self)
        #use a black pen for the grid
        qp.setPen(QColor(255,255,255))
        #get the size so we can calculate where to draw
        size = event.rect().size()

        #calculate the column's width and the row's height
        colsize = size.width() // 5
        rowsize = size.height() // 5

        #draw the two vertical lines
        qp.drawLine(colsize*2, rowsize, colsize*2, rowsize*4)
        qp.drawLine(colsize*3, rowsize, colsize*3, rowsize*4)
        #draw the two horizaontal lines
        qp.drawLine(colsize, rowsize*2, colsize*4, rowsize*2)
        qp.drawLine(colsize, rowsize*3, colsize*4, rowsize*3)

        # now, draw the tokens that are on the board
        for r in range(0,3):
            for c in range(0,3):
                if self.game.board[c][r] == 'X':
                    self.drawX(qp, c, r, colsize, rowsize)
                elif self.game.board[c][r] == 'O':
                    self.drawO(qp, c, r, colsize, rowsize)
                    
    def drawX(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        # Draw two diagonal lines in this cell
        qp.drawLine(x, y, x+colsize, y+rowsize)
        qp.drawLine(x+colsize, y, x, y+rowsize)

    def drawO(self, qp, c, r, colsize, rowsize):
        x = colsize + c*colsize
        y = rowsize + r*rowsize
        # draw an ellipse in this cell
        qp.drawEllipse(x,y,colsize, rowsize)


    #respond to mousepress events
    def mousePressEvent(self, event):
        # calculate the column width and row height
        size = self.size()
        colsize = size.width() // 5
        rowsize = size.height() // 5

        # figure which cell was clicked in based on the mouse position
        col = math.floor((event.position().x() // colsize)) - 1
        row = math.floor((event.position().y() // rowsize)) - 1

        # If the cell is in our game board, take the turn
        if col >= 0 and col < 3 and row >= 0 and row < 3:
            self.game.takeTurn(col, row)

        # force a repaint
        self.repaint()

        winner = self.game.checkForWinner()
        if winner != ' ':
            # Declare a winner and see if they want to play again
            dlg = WinnerDialog(winner)
            if dlg.exec() == True:
                # let's play again!
                self.game.clearBoard()

def main():
    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
