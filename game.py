#This program demonstrates a guessing game
from random import randint  


name = input("What's your name? ")
print("Hello, " + name + "!")


#generate a random number
random_number = randint(10,50)


counter=0
while counter <5:
    user_number = eval(input("Enter a number:"))
    counter +=1

    if user_number<random_number:
        print("your guess is too low")
    elif user_number>random_number:
        print("Your guess is too high")
    elif user_number==random_number:
        print("you win!")
        break


print ("game over")
if user_number==random_number:
    print("You win")
else :
    print("Game over! The correct number is")
    print(random_number)
    





#generate a random number
# using a while loop 
# check if user input is equal to generated number


