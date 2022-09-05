print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

direction = input("You are at a crossroad, Do you wanna go left or right? \n").lower()

if direction == "left":
    action = input("Do you wanna swim or wait? \n").lower()
    if action == "wait":
        door = input("Which door? Red, Blue or Yellow? \n").lower()
        if door == "yellow":
            print("Hoorayy!! You win!")
        else:
            print("Game Over")
    else:
        print("You drowned! Game Over.")    
else:
    print("Game Over.")

