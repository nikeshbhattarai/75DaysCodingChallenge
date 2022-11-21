print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

amount = 0

if size == "S":
    amount += 15
    if add_pepperoni == "Y":
        amount += 2

elif size == "M":
    amount += 20
    if add_pepperoni == "Y":
        amount += 3
else:
    amount += 25
    if add_pepperoni == "Y":
        amount += 3

if extra_cheese == "Y":
    amount += 1

print(f"Your final bill is : ${amount}.")



