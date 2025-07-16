from tkinter import *
from PIL import Image, ImageTk
import time




# game board spaces
game_spaces = [
    (100, 300),
    (100, 500),
    (100, 700),
    (300, 300),
    (300, 500),
    (300, 700),
    (500, 300),
    (500, 500),
    (500, 700)
    ]
buttons = []











# initialize game board and window
root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x800")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

header_img = Image.open('images/header.jpg')
header = ImageTk.PhotoImage(header_img)
cell_img = Image.open('images/cell.jpg')
cell = ImageTk.PhotoImage(cell_img)
draw_X = Image.open('images/X.png')
X_img = ImageTk.PhotoImage(draw_X)
draw_O = Image.open('images/O.png')
O_img = ImageTk.PhotoImage(draw_O)

canvas = Canvas(root, width=header.width(), height=(header.height() * 4))
canvas.grid(row=0, column=0, sticky='nsew')






def button_click(button):
    img_to_merge = Image.new('RGBA', cell_img.size)
    converted_cell = cell_img.convert('RGBA')
    img_to_merge.paste(converted_cell, (0, 0))
    x_loc = [b[1][0] for b in buttons if b[0] == button] #button[1][0]
    y_loc = [b[1][1] for b in buttons if b[0] == button] #button[1][1]
    img_to_merge.paste(draw_X, (0, 0), draw_X)
    display_img = ImageTk.PhotoImage(img_to_merge)
    display_lbl = Label(root, image=display_img, highlightthickness=0)
    display_lbl.image = display_img
    canvas.create_window(x_loc[0], y_loc[0], window=display_lbl, width=200, height=200, anchor='center')
    buttons_to_remove = next((b for b in buttons if b[0] == button), None)
    if buttons_to_remove is not None:
        buttons.remove(buttons_to_remove)

def generate_button(x, y):
    cell_button = Button(root, image=cell, highlightthickness=0, bd=0, command=lambda: button_click(button=cell_button))
    canvas.create_window(x, y, window=cell_button, width=200, height=200, anchor='center')
    buttons.append((cell_button, (x, y)))


def measure():
    return len(buttons)





canvas.create_image(0,0, image=header, anchor='nw')


for tup in game_spaces:
    for x, y in [tup]:
        row = x
        column = y
    generate_button(x=row, y=column)






root.mainloop()