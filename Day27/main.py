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
my_label.pack(side='left')

#Button
button = Button(text="Click me", command=button_clicked)
button.pack(side='left')

#Entry
input = Entry(width=10)
input.pack(side="left")


window.mainloop()
