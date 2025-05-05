'''
Assignment 2: 
Exercise 2: perfectNumber.py
Name: [Krisalda Mihali]
'''

n = int(input("Hello! Think of a number to prove it is a perfect number...\n A number is called perfect if it is equal to the sum of all of its divisors, not including the number itself.\n Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("This is a perfect number! :)")
else:
    print("This is not a perfect number! :(")
