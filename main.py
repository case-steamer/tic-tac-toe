from tkinter import *
from PIL import Image, ImageTk

















root = Tk()
root.title("Tic-Tac-Toe")

board = Image.open('images/Board.jpg')
game_board = ImageTk.PhotoImage(board)

board_label = Label(root, image=game_board)

board_label.grid(row=0, column=0)








root.mainloop()