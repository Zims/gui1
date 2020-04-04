# Find Cost of Tile to Cover W x H wall -
# Calculate the total cost of tile it would take to cover a room,
# using a cost entered by the user. Visual or ui???
import tkinter
from tkinter import *


window = tkinter.Tk()

window.title("How much?")

# label = tkinter.Label(window, text="Calculate the amount of tile needed").pack()


window.geometry('400x200')
label_1 = Label(window, text="Enter room width:").grid(column=0,row=0)
entry_1 = Entry(window).grid(column=1,row=0)
button_1 = Button(window, text="Press to enter").grid(column=1,row=1)

# bt = Button(window, text="  Enter  ")
# bt.pack()
window.mainloop()

extra_tile = 1.15

def get_lenght():
    while type(input) != int or float:
        try:
            x_lenght = float(input('*  The floor length in meters? '))
            return x_lenght
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
    sq_m = get_lenght() * get_width()
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