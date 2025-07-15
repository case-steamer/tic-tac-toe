from tkinter import *
from PIL import Image, ImageTk




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
    print(button)
    X = draw_X.convert('RGBA')
    O = O_img
    img = cell_img.convert('RGBA')
    x_loc = [b[1][0] for b in buttons if b[0] == button] #button[1][0]
    y_loc = [b[1][1] for b in buttons if b[0] == button] #button[1][1]
    xc = x_loc[0]
    yc = y_loc[0]
    x_floor = (x_loc[0] // 2)
    y_floor = (y_loc[0] // 2)
    # draw_label = Label(root, image=X, highlightthickness=0, bd=0)
    img.paste(X, (x_floor, y_floor), X)
    display_img = ImageTk.PhotoImage(img)
    # display_lbl = Label(root, width=200, height=200, image=display_img, highlightthickness=0)
    # display_lbl.image = display_img
    canvas.create_image(xc, yc, image=display_img, anchor='center')
    canvas.image  = display_img


def generate_button(x, y):
    cell_button = Button(root, image=cell, highlightthickness=0, bd=0, command=lambda: button_click(button=cell_button))
    # cell_button.grid(row=row, column=column, columnspan=1, rowspan=1, sticky='nsew')
    canvas.create_window(x, y, window=cell_button, width=200, height=200, anchor='center')
    # canvas.create_window(x, y, window=cell_button, width=200, height=400, anchor='center')
    buttons.append((cell_button, (x, y)))
    print(x,y)



canvas.create_image(0,0, image=header, anchor='nw')


for tup in game_spaces:
    for x, y in [tup]:
        row = x
        column = y
    generate_button(x=row, y=column)






if __name__ == "__main__":
    # canvas.grid(row=0, column=0)
    root.mainloop()