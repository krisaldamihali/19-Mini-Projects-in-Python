'''
Assignment 2: 
Exercise 1: RockPaperScissors.py
Name: [Krisalda Mihali]
'''

# asks users for name
print("Welcome to rock-paper-scissors!!!\n This game is played by two players.")
user1 = input("Player 1: What's your name? ")
user2 = input("Player 2: What's your name? ")

def compare(u1, u2): # tests and returns results of rock paper scissors
  if u1 == u2:
    print("It's a tie!")
  elif u1 == 'rock': # accounts for all possible results
    if u2 == 'scissors':
      print("{} won because rock beats scissors!".format(user1, user1))
    if u2 == 'paper':
      print("{} Oops...You lost because paper beats rock!".format(user1))
    
      
  elif u1 == 'scissors':
    if u2 == 'paper':
      print("{} won because scissors beats paper!".format(user1))
    if u2 == 'rock':
      print("{} Oops...You lost because rock beats scissors!".format(user1, user1))
  
  elif u1 == 'paper':
    if u2 == 'rock':
      print("{} won because paper beats rock!".format(user1))
    if u2 == 'scissors':
      print("{} Oops...You lost because scissors beats paper!!!".format(user1))
    
  else: # rejects all other responses
    print("Oops...Try again!!!!Thanks for playing! :)")
    
def game():
    
  # asks users for rock/paper/scissors
  user1_choice = input("\n{}, do you choose rock, paper or scissors? ".format(user1)).lower()
  user2_choice = input("{}, do you choose rock, paper or scissors? ".format(user2)).lower()
    
  compare(user1_choice, user2_choice)
  # asks user if they want to play again
    
game()



