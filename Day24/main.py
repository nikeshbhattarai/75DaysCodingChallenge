# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", "w") as file:
#     file.write("New text.")

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)