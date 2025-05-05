'''
Assignment 1: 
Exercise 2: (calculatorBMI.py)
Write a program that prompts the user to enter a weight and height then displays the BMI.

Name: [Krisalda Mihali]
'''

print ("Find out your BMI (Body Mass Index)")
weightkg = input ("Enter your weight in kilograms:")
heightMeters = input ("Enter your height in meters:")
k = int(weightkg)
m = float(heightMeters)
BMI = k / m ** 2
BMI = round (BMI , 2)
print ("Your BMI is " +str(BMI)) #BMI result

#Conditions to give the result of a measure of health on weight.
if BMI < 18.5: #Condition to be considered underweight.
  print ("Be careful! You are underweight. Pay attention to what you eat or what you drink. Get tips on how to become healthy!")
elif 18.5 <= BMI < 25.0: #Condition to be considered normal.
  print ("You are normal. Keep maintaining your weight! ")
elif 25.0 <= BMI < 30.0: #Condition to be considered overweight.
  print ("Be careful! You are overweight. Pay attention to what you eat or what you drink. Get tips on how to become healthy!")
elif 30.0 <= BMI: #Condition to be considered obese.
  print ("Oops ... You are obese. You are not healthy. Consult a doctor immediately about your health!")
