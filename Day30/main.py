try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["abc"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")