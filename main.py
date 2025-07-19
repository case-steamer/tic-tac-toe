import tkinter
from tkinter import *
from PIL import Image, ImageTk
import time
from player import Player




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
count = 1








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

p1 = Player(name='Player 1', avatar=draw_X, status='')
p2 = Player(name='Player 2', avatar=draw_O, status='')





def check_vertical(cell_list: list):
    tick = None
    one = 0
    two = 0
    three = 0
    for cell in cell_list:
        if cell[1] == 300:
            one += 1
        elif cell[1] == 500:
            two += 1
        elif cell[1] == 700:
            three += 1
    ticks = [one, two, three]
    for t in ticks:
        if t == 3:
            tick = True
            break
    if not tick:
        tick = False
    return tick


def check_horizontal(cell_list: list):
    tick = None
    one = 0
    two = 0
    three = 0
    for cell in cell_list:
        if cell[0] == 100:
            one += 1
        elif cell[0] == 300:
            two += 1
        elif cell[0] == 500:
            three += 1
    ticks = [one, two, three]
    for t in ticks:
        if t == 3:
            tick = True
            break
    if not tick:
        tick = False
    return tick


def check_diagonal(cell_list:list):
    p_ticks = 0
    n_ticks = 0
    x_coords = [num for num in range(100, 600, 200)]
    y_coords = [num for num in range(300, 800, 200)]
    for cell in cell_list:
        for r in range(3):
            if cell[0] == x_coords[r] and cell[1] == y_coords[r]:
                p_ticks += 1
    if p_ticks != 3:
        x_coords = list(reversed(x_coords))
        for cell in cell_list:
            for r in range(3):
                if cell[0] == x_coords[r] and cell[1] == y_coords[r]:
                    n_ticks += 1
                    print(n_ticks)
    if n_ticks == 3:
        return n_ticks
    elif n_ticks != 3 and p_ticks == 3:
        return p_ticks
    else:
        return None


def check_for_three(player:Player):
    tick = None
    if check_vertical(player.cells):
        player.status = "wins!"
        tick = True
    elif not check_vertical(player.cells):
        if check_horizontal(player.cells):
            player.status = "wins!"
            tick = True
        elif not check_horizontal(player.cells):
            if check_diagonal(player.cells) == 3:
                player.status = 'wins!'
                tick = True
    if not tick:
        tick = False
    return tick


def button_click(button):
    global count
    if count % 2 == 0:
        current_player = p2
    else:
        current_player = p1
    avi_img = current_player.avatar
    img_to_merge = Image.new('RGBA', cell_img.size)
    converted_cell = cell_img.convert('RGBA')
    img_to_merge.paste(converted_cell, (0, 0))
    x_loc = [b[1][0] for b in buttons if b[0] == button] #button[1][0]
    y_loc = [b[1][1] for b in buttons if b[0] == button] #button[1][1]
    img_to_merge.paste(avi_img, (0, 0), avi_img)
    display_img = ImageTk.PhotoImage(img_to_merge)
    display_lbl = Label(root, image=display_img, highlightthickness=0)
    display_lbl.image = display_img
    canvas.create_window(x_loc[0], y_loc[0], window=display_lbl, width=200, height=200, anchor='center')
    button_to_remove = next((b for b in buttons if b[0] == button), None)
    if button_to_remove is not None:
        current_player.cells.append(button_to_remove[1])
        buttons.remove(button_to_remove)
    if check_for_three(current_player):
        print(current_player.name + ' ' + current_player.status)
    if current_player.status == 'wins!':
        for button in buttons:
            button[0].config(state=tkinter.DISABLED)
        current_player.score += 1
        p1_lab.config(text=p1.update())
        p2_lab.config(text=p2.update())
    count += 1


def generate_button(x, y):
    cell_button = Button(root, image=cell, highlightthickness=0, bd=0, command=lambda: button_click(button=cell_button))
    canvas.create_window(x, y, window=cell_button, width=200, height=200, anchor='center')
    buttons.append((cell_button, (x, y)))








canvas.create_image(0,0, image=header, anchor='nw')
p1_lab = Label(root, text=p1.update(), font=('lato', 14), bg='#169222')
p2_lab = Label(root, text=p2.update(), font=('lato', 14), bg='#169222')

canvas.create_window(60, 100, window=p1_lab)
canvas.create_window(60, 180, window=p2_lab)


for tup in game_spaces:
    for x, y in [tup]:
        row = x
        column = y
    generate_button(x=row, y=column)






root.mainloop()