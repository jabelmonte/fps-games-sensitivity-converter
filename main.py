from tkinter import *

from conversion import Conversion

root = Tk()
csgo_sensitivity = 10.00
valorant_sensitivity = 10.00

convert = Conversion()

csgo_result = convert.csgo_to_valorant(csgo_sensitivity)
valorant_result = convert.valorant_to_csgo(valorant_sensitivity)

def do_convert():
    label = Label(root, text=csgo_result)
    label.pack()

button_convert = Button(root, text="convert", padx=20, command=do_convert)
button_convert.pack()
root.mainloop()