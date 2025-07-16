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
xos = 0
xts = 0
xfs = 0
yts = 0
yfs = 0
yss = 0











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


def check_for_three(player:Player, cell_x, cell_y):
    print((cell_x, cell_y))
    global xos
    global xts
    global xfs
    global yts
    global yfs
    global yss
    x_local = [num for num in range(100, 600, 200)]
    y_local = [num for num in range(300, 800, 200)]
    print(x_local)
    print(y_local)
    for num in x_local:
        if cell_x == num and num == 100:
            xos += 1
            # break
        elif cell_x == num and num == 300:
            xts += 1
            # break
        elif cell_x == num and num == 500:
            xfs += 1
            # break
    for y in y_local:
        if cell_y ==  y and y == 300:
            yts += 1
            # break
        elif cell_y == y and y == 500:
            yfs += 1
            # break
        elif cell_y == y and y == 700:
            yss += 1
            # break
    x_cell_score = [xos, xts, xfs]
    y_cell_score = [yts, yfs, yss]
    print(x_cell_score)
    print(y_cell_score)
    if sum(x_cell_score) == sum(y_cell_score) == 3:
        player.status = 'wins'
        marker = True
    else:
        for x in x_cell_score:
            for y in y_cell_score:
                if x != 3 and y != 3:
                    marker = False
                else:
                    player.status = 'wins!'
                    marker = True
    print(marker)
    return marker



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
    if check_for_three(current_player, x_loc, y_loc):
        print(current_player.name + ' ' + current_player.status)
    count += 1

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