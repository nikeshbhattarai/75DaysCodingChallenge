from tkinter import *

def button_clicked():
    print("Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window =  Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.config(text="Label")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

# New Button 
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)
#Entry
input = Entry(text="Entry", width=10)
input.grid(column=3, row=3)


window.mainloop()
