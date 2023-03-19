# import tkinter

# window =  tkinter.Tk()
# window.title("First GUI Program")
# window.minsize(width=500, height=300)

# #Label
# my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label.pack()
# window.mainloop()
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

tot = add(3,4,5,8,10,20)
print(tot)


import ast

def parse_list(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == list:
            return s
        return
    except:
        return
    
# zones = [
#         {
#             "name": "101A",
#             "points": "[(90, 165), (169, 165), (107, 338), (5, 319)]",
#             "position": "center"
#         },
#         {
#             "name": "102",
#             "points": "[(202, 142), (258, 59), (379, 60), (446, 136), (397, 139), (373, 89), (263, 92), (255, 139)]",
#             "position": "center"
#         },
#         {
#             "name": "103A",
#             "points": "[(394, 166), (476, 160), (537, 319), (468, 326)]",
#             "position": "center"
#         },
#         {
#             "name": "101B",
#             "points": "[(205, 165), (246, 165), (224, 335), (166, 333)]",
#             "position": "center"
#         },
#         {
#             "name": "103B",
#             "points": "[(502, 172), (538, 169), (621, 315), (573, 318)]",
#             "position": "center"
#         }
#     ]

# cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)