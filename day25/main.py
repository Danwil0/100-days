# with open("weather_data.csv") as file:
#     data = file.readlines()
#

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         temperature.append(row[1])
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data["temp"])
# temp_list = data["temp"].to_list()
# # # cache = 0
# #
# for num in temp_list:
#     cache += num
# average = cache / len(temp_list)
# print(average)

# get data in row
# print(data[data.day == "monday"])
# print(data[data["temp"] == data["temp"].max()])

#
# monday = data[data.day == "monday"]
# monday_temp = monday.temp[0]

# create a dataframe from scratch
# data_dict = {
#     "students": ["amy", "james", "angela"]
#     "scores": [78, 89, 50]
# }
data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
#

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color = squirrel_data["Primary Fur Color"].to_list()

gray_col = 0
cinnamon = 0
black = 0
#print(squirrel_color)
for color in squirrel_color:
    if color == "Gray":
        gray_col += 1

    if color == "Cinnamon":
        cinnamon += 1

    if color == "Black":
        black += 1

dict_list = {
    "color": ["cinnamon", "gray", "black"],
    "count": [f"{cinnamon}", f"{gray_col}", f"{black}"],
}

new_data = pandas.DataFrame(dict_list)
print(new_data)
new_data.to_csv("squirrel_data.csv")




















