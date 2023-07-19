# with open("weather_data.csv") as data_file:
#     data = data_file.read().splitlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # for index, row in enumerate(data):
#     for row in data:
#         # if index != 0:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

"""Sacamos el promedio"""
# def average_temp(list):
#     if len(list) == 0:
#         return 0
#     else:
#         suma = sum(list)
#         tamano_lista = len(list)
#         resultado = suma / tamano_lista
#         return resultado
#
#
# temp_promedio = average_temp(temp_list)
# print(round(temp_promedio, 2))

"""Promedio Con pandas"""
# temp_promedio = data["temp"].mean()
# print(round(temp_promedio, 2))

"""Temp maxima con Pandas"""
# max_temp = data["temp"].max()
# print(max_temp)

"""Get data in columns"""
# print(data["condition"])
# print(data.condition)

"""Get data in rows"""
# print(data[data.day == "Monday"])

"""Challenge: Print the row of data which had the highest temperature"""
# max_temp = data["temp"].max()
# row_max_temp = data[data.temp == max_temp]
#
# print(row_max_temp)

"""Challenge Convert Monday Temperature to Farenheit"""
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp[0])
monday_f = (monday_temp * 9/5) + 32
# print(monday_f)

"""Create a Data frame from scratch"""
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
