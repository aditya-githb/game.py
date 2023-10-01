import random

choice = ['rock', 'paper', 'scissor']

while True:

    print("Welcome to the Rock, Paper Scissors Game \n")

    score = int(0)

    while True:

        

        print(f"score = {score}")

        user = input("Enter your Choice(use small case): ")

        comp = random.choice(choice)

        print(f"\nYou choose {user} and Computer choose {comp} \n")

        if (user == 'rock' and comp == 'scissors') or \
           (user == 'paper' and comp == 'rock') or \
           (user == 'scissors' and comp == 'paper'):
            print("You win!")
            score += 2

        elif user == comp:
            print("It's a tie!")
            score += 1

        else:
            print("You lose!")
            break
    
    play = input("Play Again? (y/n): ")

    if play == "y":
        print()
    else:
        break
