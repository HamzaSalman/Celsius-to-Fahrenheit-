# Created by: Hamza Salman
# Created on: October 2016
# Course: ICS3U
# This program converts Fahrenheit to celcius

print('enter temprature in degrees fahrenheit')
celcius = float(raw_input())

def calculate_fahrenheit(celcius_input):
	
    fahrenheit = 1.8 * celcius_input + 32
    
    print(str(fahrenheit) + ' is the temprature in fahrenheit.')

calculate_fahrenheit(celcius)
