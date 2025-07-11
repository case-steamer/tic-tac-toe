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


def button_click(button):
    print(button)
    X = X_img
    O = O_img
    x_loc = [b[1][0] for b in buttons if b[0] == button] #button[1][0]
    y_loc = [b[1][1] for b in buttons if b[0] == button] #button[1][1]
    label = Label(root, image=X, highlightthickness=0, bd=0)
    label.grid(row=x_loc, column=y_loc, columnspan=1, rowspan=1, sticky='nsew')


def generate_button(x, y):
    cell_button = Button(root, image=cell, highlightthickness=0, bd=0, command=lambda: button_click(button=cell_button))
    cell_button.grid(row=row, column=column, columnspan=1, rowspan=1, sticky='nsew')
    buttons.append((cell_button, tup))



board_label = Label(root, image=header, highlightthickness=0)


board_label.grid(row=0, column=0, columnspan=3, rowspan=1, sticky='nsew')

for tup in game_spaces:
    for x, y in [tup]:
        row = x
        column = y
    generate_button(x=row, y=column)






if __name__ == "__main__":
    root.mainloop()