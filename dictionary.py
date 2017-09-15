#!/usr/bin/python3

user = {"name":"Masha", "age": 24, "have_airplane": False}
print (user)

print (len(user))

print (user["name"])

print (user.get("name1"))

weather = {"city":"Москва", "temperature": 24, "wind":"восточный"}
print(weather["city"])

weather["temperature"] = 29
print(weather["temperature"])

print(len(weather))

weather["date"] = "27.05.2017"
print (weather)

my_weather_list = []
my_weather_list.append(weather)


my_weather_list.append({"name":"Masha", "age": 21, "have_airplane": False, "date": "28.05.2017"})
my_weather_list.append({"name":"Masha", "age": 23, "have_airplane": False, "date": "29.05.2017"})

print(my_weather_list)



