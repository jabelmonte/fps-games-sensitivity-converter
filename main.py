from tkinter import *
from conversion import Conversion


root = Tk()
convert = Conversion()
input_current_sensitivity = Entry(root)
change_to = IntVar()
Radiobutton(root, text="Valorant", variable=change_to, value=1).pack()
Radiobutton(root, text="CSGO", variable=change_to, value=2).pack()

def do_convert():
    current_sensitivity_in_string = input_current_sensitivity.get()
    current_sensitivity = int(current_sensitivity_in_string)
    game_choice = change_to.get()
    if game_choice == 1:
        result =0.0
        result = convert.csgo_to_valorant(current_sensitivity)
        label = Label(root, text=result)
        label.pack()
        
    elif game_choice == 2:
        result =0.0
        result = convert.valorant_to_csgo(current_sensitivity)
        label = Label(root, text=result)
        label.pack()

button_convert = Button(root, text="convert", padx=20, command=do_convert)
input_current_sensitivity.pack()
button_convert.pack()
root.mainloop()