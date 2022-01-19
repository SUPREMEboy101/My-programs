import random

#generates a random number for the user to guess
random_num = random.randint(1, 100)

#ask the user to enter how many times they would like to attempt and stores it in the "attempts" variable
attempts = int(input("Enter how many times you would like to attempt: "))

#loops till they run out of attempts
while (attempts != 0):

    #prompts user to enter a guess
    guess = int(input("Enter your guess: "))
    
    #decreases the number of attempts after each guess
    attempts -= 1
    
    if (attempts == 0):
        print("You are out of attempts :(")
    
    elif (guess == random_num):
        print("You guessed it right!")

        #this break statement terminates the while loop when the user guesses correctly
        break
    
    elif (guess != random_num):
        if (guess > random_num):
            print("Guess lower")
        else:
            print("Guess higher")
        
        print("Attempts remaining: " + str(attempts))