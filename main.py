from tkinter import *
from PIL import Image, ImageTk





# game board spaces
game_spaces = [
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (3, 0),
    (3, 1),
    (3, 2)
    ]
buttons = []





def button_click(image, coords):
    label = Label(root, image=image, highlightthickness=0, bd=0)
    for x,y in [coords]:
        button = [b for b in buttons if b[1] == x,y]









# initialize game board and window
root = Tk()
root.title("Tic-Tac-Toe")


header_img = Image.open('images/header.jpg')
header = ImageTk.PhotoImage(header_img)
cell_img = Image.open('images/cell.jpg')
cell = ImageTk.PhotoImage(cell_img)
draw_X = Image.open('images/X.png')
X_img = ImageTk.PhotoImage(draw_X)
draw_O = Image.open('images/O.png')
O_img = ImageTk.PhotoImage(draw_O)

board_label = Label(root, image=header, highlightthickness=0, bd=0)


board_label.grid(row=0, column=0, columnspan=3, rowspan=1, sticky='nsew')

for tup in game_spaces:
    cell_button = Button(root, image=cell, highlightthickness=0, bd=0)
    for x, y in [tup]:
        row = x
        column = y
    cell_button.grid(row=row, column=column, columnspan=1, rowspan=1, sticky='nsew')
    buttons.append((cell_button, tup))







root.mainloop()