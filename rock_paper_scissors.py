import random

exit = False
user_points = 0
computer_points = 0

while exit  == False:

    options = ["rock","paper","scissors"]
    user_input = input("Choose rock, paper or scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print(f'Your points: {user_points}, Computer points: {computer_points}')
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Its a Tie! ")   
        elif computer_input == "paper":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Computer Wins! ")
            computer_points += 1  
        elif computer_input == "scissors":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Player Wins! ")
            user_points += 1   

    if user_input == "paper":
        if computer_input == "paper":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Its a Tie! ")   
        elif computer_input == "scissors":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Computer Wins! ")
            computer_points += 1  
        elif computer_input == "rock":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Player Wins! ")
            user_points += 1    

    if user_input == "scissors":
        if computer_input == "scissors":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Its a Tie! ")   
        elif computer_input == "rock":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Computer Wins! ")
            computer_points += 1  
        elif computer_input == "paper":
            print(f'Your input is {user_input}, computer input is {computer_input}') 
            print("Player Wins! ")
            user_points += 1   

    elif user_input not in ["paper","scissors","rock","exit"]:
        print("Invalid Input!")        



