name = input("Enter your name: ")
surname = input("Enter your surname: ")

def format_name(f_name, l_name):
    if f_name == "" or l_name = "":
        return "You didn't provide valid inputs."
    f_name = f_name.title()
    l_name = surname.title()
    return f_name, l_name

first_name, last_name = format_name(name, surname)
print(f"Your name is {first_name} {last_name}.")
