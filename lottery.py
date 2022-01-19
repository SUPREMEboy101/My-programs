import random

#random numbers are picked from this array
choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#generates two numbers for the user
def generate_user_lottery_num():
  num1 = random.choice(choice)
  num2 = random.choice(choice)
  print("Your lottery Numbers are: " + str(num1) + " & " + str(num2))
  return num1, num2

#generates two lottery numbers and returns them
def generate_lottery_num():
  num1  = random.choice(choice)
  num2  = random.choice(choice)
  print("Winning lottery Numbers are: " + str(num1) + " & " + str(num2))
  return num1, num2

#lottery numbers and user numbers are initialized here by using the returned values from the functions
user_num1, user_num2 = generate_user_lottery_num()
lottery_num1, lottery_num2 = generate_lottery_num()

#checks if the two digits match
if ( (user_num1 == lottery_num1) & (user_num2 == lottery_num2) ):
  print("Both digits have matched! You won the lottery! Your Prize money: $1 Lakh")

#checks if at least one digit matches (order matters)
elif ( (user_num1 == lottery_num1) or (user_num2 == lottery_num2) ):
  print("1 digit has matched! You won the lottery! Your Prize money: $30,000")

#executes if none match
else :
  print("No digits have matched. Better luck next time. Your Prize money: $0")