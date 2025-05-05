'''
Assignment 3: 
Exercise 1: Take a number from the user. Find the first element which is bigger than the input and inset the input
before that element.
Name: [Krisalda Mihali]
'''
import bisect
userinput=int(input("Enter a number.")) #Enter a number 
list=[1,6,3,6,9] #Create the list.
bisect.insort(list, userinput)
print(list)#Print the list
