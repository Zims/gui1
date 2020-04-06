# Find Cost of Tile to Cover W x H wall -
# Calculate the total cost of tile it would take to cover a room,
# using a cost entered by the user. Visual or ui???
import tkinter
from tkinter import *


window = tkinter.Tk()

window.title("How much?")

# label = tkinter.Label(window, text="Calculate the amount of tile needed").pack()

def room_size():
    entered_width = float(width.get())
    entered_length = float(length.get())
    sqf = entered_length * entered_width
    size_text = str(sqf)
    pass

window.geometry('500x350')
top_bar = Label(window, text=" ").grid(column=1, row=0)
width = Label(window, text="Enter room width:").grid(column=0, row=1)
length = Label(window, text="Enter room length:").grid(column=0, row=2)
get_width_label = Entry(window).grid(column=1, row=1)
get_length_label = Entry(window).grid(column=1, row=2)
enter_size = Button(window, text="Get the size of the room", command=room_size).grid(column=1, row=5)
size_label = Label(window, text="The square footage is:").grid(column=1, row=6)
size_result = Label(window, text="result of x * y placeholder").grid(column=1, row=7)
size_suggestion = Label(window, text="Industry standard is adding 15% more. That is: ").grid(column=1, row=8)
size_fixed = Label(window, text="x * y * 1.15").grid(column=1, row=9)
set_price = Label(window, text="Price of tile:").grid(column=0, row=10)
tile_price = Entry(window).grid(column=1, row=10)
enter_size = Button(window, text="Get total expenses").grid(column=1, row=11)
complete_cost_label = Label(window, text="The complete cost: ").grid(column=1, row=12)
complete_cost = Label(window, text="SUM placeholder").grid(column=1, row=13)


window.mainloop()

extra_tile = 1.15



def get_length():
    while type(input) != int or float:
        try:
            x_length = float(input('*  The floor length in meters? '))
            return x_length
        except ValueError:
            print('Sorry, use a number! (50cm = 0.5)')


def get_width():
    while type(input) != int or float:
        try:
            y_width = float(input('*  The floor width in meters? '))
            return y_width
        except ValueError:
            print('Sorry, use a number! (50cm = 0.5)')
        else:
            print(y_width)


def get_price():
    sq_m = get_length() * get_width()
    price_sqm = None
    while type(price_sqm) != int or float:
        try:
            price_sqm = float(input('*  The price per sqm? '))
        except ValueError:
            print('Sorry, price in USD!')
        else:
            print('*'*60)
            extra = round(sq_m * extra_tile, 2)
            print(f'*  You raw diameters are {sq_m} sq/m but we advise 15% extra. \n*  That is {extra} sq/m\n')
            whole_price = round(sq_m * 1.15 * price_sqm, 2)

            print(':'*60)
            print(f'''      ✅ The whole price is {whole_price} USD.✅
            \n* Type in different price or press Ctrl + C to exit 
            \n* or start over for different room.\n''')
            print('\\../'*15)


get_price()
