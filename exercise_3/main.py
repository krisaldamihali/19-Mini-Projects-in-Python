'''
Assignment 3: 
Exercise 3: Given a list of countries and cities of each country from the user, then given the names of the cities.
For each city print the country in which it is located.
Name: [Krisalda Mihali]
'''
cities_dict = {"Tirana":"Albania","Lushnje":"Albania","Durresi":"Albania","Vlora":"Albania","Paris":"France","Nice":"France","Montepellier":"France","Berlin":"Germany","Frankfurt":"Germany","Munich":"Germany"} #Declare a static dict
userinput = input("Pick a city:") #Pick a city.
while userinput != "stop": #Create while loop
  if userinput not in cities_dict:#Create conditions
    print("Sorry, this city is not in our dictionary. Try a different one.")
  else:
    print(userinput + "=>"+ cities_dict.get(userinput))#Print the result
  userinput = input("Pick a city:")