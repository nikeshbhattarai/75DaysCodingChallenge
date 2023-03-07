#import csv
import pandas as pd

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# df = pd.read_csv("weather-data.csv")

# temp_list = df["temp"].to_list()
# print(temp_list)

# average = sum(temp_list)/len(temp_list)


# print(df["temp"].mean())

# print(df["temp"].max())
# max_temp = df["temp"].max()

# print(df[df["temp"] == df["temp"].max()])

# monday = df[df.day == "Monday"]
# print(monday.temp)
# temp_in_f = (1.8 * int(monday.temp)) + 32
# print(temp_in_f)

df = pd.read_csv("squirrel_data.csv")
print(df["Primary Fur Color"])
print(df["Primary Fur Color"].unique())

grey_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)

cinnamon_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_squirrels_count)

black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])
print(black_squirrels_count)
print(type(black_squirrels_count))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

print(data_dict)

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")





