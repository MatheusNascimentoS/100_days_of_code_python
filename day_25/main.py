# import csv

# with open(r"day_25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv(r"day_25\weather_data.csv")
# # temp_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(data["temp"].max())

# celsius = float(data[data.day == "Monday"].temp)
# print(celsius)
# fahrenheit = (celsius * 9 / 5) + 32
# print(fahrenheit)

data = pandas.read_csv(r"day_25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv(r"day_25\squirrel_count.csv")