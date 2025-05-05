'''
Assignment 1: 
Exercise 3: (leapYear.py) 
Write a program that prompts the user  to enter a year between 1500 and 2020 and then reports whether it is a leap year.

Name: [Krisalda Mihali]
'''

year=int(input('Enter a year between 1500-2020:')) 
#Conditions to distinguish whether it is a leap year or not.
if year >= 1500 and year <= 2020:
  if year % 100 == 0 and year % 400 == 0:
    print('It is a leap year. February has 29 days. ')
  elif year % 4 == 0 and year % 100 != 0:
    print('It is a leap year. February has 29 days. ')
  else:
    print('It is not a leap year. February has 28 days.')
#If the year is out the range , will print an error message.
if year < 1500 or year > 2020:
  print("Error message!!! :( Enter a year between 1500-2020.")

