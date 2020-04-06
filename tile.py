# Find Cost of Tile to Cover W x H wall -
# Calculate the total cost of tile it would take to cover a room,
# using a cost entered by the user. Visual or ui???
import tkinter
from tkinter import *


window = tkinter.Tk()

window.title("How much?")

# label = tkinter.Label(window, text="Calculate the amount of tile needed").pack()

def room_size():
    entered_w = int(get_width_label.get())
    entered_l = int(get_length_label.get())
    tile_calc = entered_l * entered_w
    print(tile_calc)
    return tile_calc
    pass


def just_check():
    print('test')

window.geometry('500x350')
top_bar = Label(window, text=" ").grid(column=1, row=0)

width = Label(window, text="Enter room width:")
width.grid(column=0, row=1)


length = Label(window, text="Enter room length:")
length.grid(column=0, row=2)

get_width_label = Entry(window)
get_width_label.grid(column=1, row=1,  sticky=W)

get_length_label = Entry(window)
get_length_label.grid(column=1, row=2)

enter_size = Button(window, text="Get the size of the room", command=room_size)
enter_size.grid(column=1, row=5)

size_label = Label(window, text="The square footage is:")
size_label.grid(column=1, row=6)

size_result = Label(window, text=room_size)
size_result.grid(column=1, row=7)

size_suggestion = Label(window, text="Industry standard is adding 15% more. That is: ")
size_suggestion.grid(column=1, row=8)

size_fixed = Label(window, text="x * y * 1.15")
size_fixed.grid(column=1, row=9)

set_price = Label(window, text="Price of tile:")
set_price.grid(column=0, row=10)

tile_price = Entry(window).grid(column=1, row=10)

enter_size = Button(window, text="Get total expenses")
enter_size.grid(column=1, row=11)

complete_cost_label = Label(window, text="The complete cost: ")
complete_cost_label.grid(column=1, row=12)

complete_cost = Label(window, text="SUM placeholder")
complete_cost.grid(column=1, row=13)


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
