
import pandas

data = pandas.read_csv("weather_data.csv")

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge: Monday's temp in Fahrenheit:

print(f"Celcius temp is: {monday.temp}")

Fahrenheit_conversion = monday.temp*(9 / 5) + 32

print(f"Fahrenheit temp is: {Fahrenheit_conversion}")
# def convert_celcius_into_fahrenheit():


#Create DataFrame from scratch:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict)
print(data2)


data2.to_csv("new_data.csv")
