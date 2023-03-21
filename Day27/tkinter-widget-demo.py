from tkinter import *

window =  Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New text")

def button_clicked():
    print("Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()



#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spibox.
    print(spinbox.get())

spinbox =  Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", 
                          variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()



window.mainloop()