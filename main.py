from tkinter import *
from conversion import Conversion

result =0.0
rows = 5
columns = 7

root = Tk()
root.title("FPS Mouse Sensitivity Converter")
root.minsize(360, 240)
root.maxsize(360, 240)
convert = Conversion()
result_sensitivity = Entry(root,  text=result)
input_current_sensitivity = Entry(root)
change_to = IntVar()

label_input_sensitivity = Label(root, text="Input your current sensitivity")
label_result = Label(root, text="Result")
label_convert_for_what_game = Label(root, text= "Convert for what game?")

Radiobutton(root, text="Valorant", variable=change_to, value=1).grid(row=2, column=1)
Radiobutton(root, text="CSGO", variable=change_to, value=2).grid(row=1, column=1)
label_convert_for_what_game.grid(row=1, column=0)
label_input_sensitivity.grid(row=3, column=0)
label_result.grid(row=5, column=0)
result_sensitivity.grid(row=5, column=1)

# adding a bit of responsiveness on the window
for i in range(rows):
    root.grid_rowconfigure(i, weight=1)
for i in range(columns):
    root.grid_columnconfigure(i, weight=1)

# converting user input at press of button
def do_convert():
    current_sensitivity_in_string = input_current_sensitivity.get()
    current_sensitivity = int(current_sensitivity_in_string)
    game_choice = change_to.get()
    if game_choice == 1:
        result = convert.csgo_to_valorant(current_sensitivity)
        result_sensitivity.delete(0, 'end')
        result_sensitivity.insert(0, result)
        
    elif game_choice == 2:
        result = convert.valorant_to_csgo(current_sensitivity)
        result_sensitivity.delete(0, 'end')
        result_sensitivity.insert(0, result)

button_convert = Button(root, text="convert", padx=20, command=do_convert)
input_current_sensitivity.grid(row=3, column=1)
button_convert.grid(row=7, column=1)
root.mainloop()