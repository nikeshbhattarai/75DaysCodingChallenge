from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg='white')

canvas = Canvas(width=200, height=200, bg='white')
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)

website_entry = Entry(width=35, bg="white")
website_entry.grid(column=1, row=1)

email = Label(text="Email/Username: ")
email.grid(column=0, row=2)

email_entry = Entry(width=35, bg="white")
email_entry.grid(column=1, row=2)

password = Label(text="Password: ")
password.grid(column=0, row=3)

password_entry = Entry(width=21, bg="white")
password_entry.grid(column=1, row=3)
# reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
# reset_button.grid(column=2, row=2)


window.mainloop()