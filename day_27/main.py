from sys import is_finalizing
import tkinter 
from tkinter import Button, Entry, font

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal_to.grid(column=0, row=1)


miles_to_km = tkinter.Label(text="0", font=("Arial", 12))
miles_to_km.grid(column=1, row=1)

km = tkinter.Label(text="km", font=("Arial", 12))
km.grid(column=2, row=1)

def button_clicked():
    miles_input = float(input.get())
    result = miles_input * 1.609
    miles_to_km.config(text=result)
    

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()

