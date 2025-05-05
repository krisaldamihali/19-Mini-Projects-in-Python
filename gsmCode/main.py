'''
Assignment 1: 
Exercise 1: gsmCode.py
Write a program that prompts the user to enter 12-digit strings as a typical mobile number in ALBANIA

Name: [Krisalda Mihali]
'''

num = str(input("Enter a 12-digit Albanian telephone number:"))
Country_code = num[0:3] #Extract the 3-digit country telephone code as separate string.
Gsm= num[3:6] #Extract the 3-digit GSM code as separate string.
PhoneNr1 = num[6:9] #Extract the remaining 6-digit number as separate string.
PhoneNr2 = num[9:12]
print("The country code is: " + Country_code)
print("The GSM code is: " + Gsm )
print("The number is: " + PhoneNr1 + PhoneNr2)
print("The phone number is:""(" + str(Country_code) + ")" "-"+ Gsm  + "-" + PhoneNr1 + "-" + PhoneNr2) #Print all number...


