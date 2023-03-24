from tkinter import *

def button_clicked():
    value_miles = input.get()
    value_km = float(value_miles) * 1.60934
    label_3.config(text=f"{value_km}")


window =  Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# #Label
# my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label.config(text="Label")
# my_label.grid(column=0, row=0)

# #Button
# button = Button(text="Button", command=button_clicked)
# button.grid(column=1, row=1)

# # New Button 
# new_button = Button(text="New Button", command=button_clicked)
# new_button.grid(column=2, row=0)
# #Entry
# input = Entry(text="Entry", width=10)
# input.grid(column=3, row=3)

input = Entry(text="Entry", width=10)
input.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Arial", 24, "bold"))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Arial", 24, "bold"))
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=("Arial", 24, "bold"))
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=("Arial", 24, "bold"))
label_4.grid(column=2, row=1)
 
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
