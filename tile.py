# Find Cost of Tile to Cover W x H wall -
# Calculate the total cost of tile it would take to cover a room,
# using a cost entered by the user. Visual or ui???
# TODO Enter not working
# TODO app that can be installed

import tkinter.messagebox
from tkinter import *

window = tkinter.Tk()

window.title("How much?")


def room_size():
    entered_w = int(get_width_label.get())
    entered_l = int(get_length_label.get())
    tile_calc = entered_l * entered_w
    size_result["text"] = tile_calc
    size_fixed_math = round(tile_calc * 1.15, 2)
    size_fixed["text"] = size_fixed_math

    return size_fixed_math

def onclick(event=None):
    room_size()
    print("You clicked the button")


window.bind('<Return>', onclick)


def complete_cost():
    tile_price_entered = float(tile_price.get())
    the_sum = round(room_size() * tile_price_entered, 2)
    complete_cost["text"] = the_sum
    complete_cost_label["text"] = "USD"


window.geometry('500x350')
top_bar = Label(window, text=" ")
top_bar.grid(column=1, row=0)

width = Label(window, text="Enter room width (in feet):")
width.grid(column=0, row=1)


length = Label(window, text="Enter room length (in feet):")
length.grid(column=0, row=2)

get_width_label = Entry(window)
get_width_label.grid(column=1, row=1)

get_length_label = Entry(window)
get_length_label.grid(column=1, row=2)

enter_size = Button(window, text="How much I need?", command=onclick)
enter_size.grid(column=1, row=5)

size_label = Label(window, text="The square footage is:")
size_label.grid(column=1, row=6)

size_result = Label(window)
size_result.grid(column=1, row=7)

size_suggestion = Label(window, text="Industry standard is adding 15% more. That is: ")
size_suggestion.grid(column=1, row=8)

size_fixed = Label(window, font=('bold', 18))
size_fixed.grid(column=1, row=9)

set_price = Label(window, text="Price of tile (in USD):")
set_price.grid(column=0, row=10)

tile_price = Entry(window)
tile_price.grid(column=1, row=10)

enter_size = Button(window, text="Get total expenses", command=complete_cost)
enter_size.grid(column=1, row=11)

complete_cost_label = Label(window, text="The complete cost: ")
complete_cost_label.grid(column=1, row=12)

complete_cost = Label(window, font=('bold', 22))
complete_cost.grid(column=1, row=13)

complete_cost_label = Label(window)
complete_cost_label.grid(column=1, row=14)


window.mainloop()
#
# Create app:
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' tile.py