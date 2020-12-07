"""

Name:		problem1.py
Purpose:	compute the temperature in celsius to fahrenheit and output it to the user.

Author:	Wang.J

Created:	date in 07/12/2020

"""
print ("**** Welcome to the celsius to fahrenheit ****")

# get the temperature in celsius from the UserWarning
celsius_temperature = float(input("Enter the temperature in celsius: "))

# compute the temperature in celsius to fahrenheit
fahrenheit = float(celsius_temperature*(9/5) + 32)

# output the converted fahrenheit temperature
print ("The temperature in fahrenheit is: " + str(fahrenheit))