
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")

selected_row = map[int(position[1])-1]
selected_row[int(position[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

