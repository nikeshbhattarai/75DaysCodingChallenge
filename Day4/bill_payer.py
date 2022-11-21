import random
names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")

number=random.randint(0, len(names)-1)
print(f"{names[number]} will be buying the meal today.")
    
# print(f"{random.choices(names)} will be buying the meal today.")
