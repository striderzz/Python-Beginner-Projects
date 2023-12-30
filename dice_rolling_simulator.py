import random

def rollDice():
  roll = input("Do you want to roll dice (Y/N)? :\n")
  
  dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
  }
  if roll.lower() == "y":
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    
    print(f'First number is {num1}, second number is {num2}')
    print("\n".join(dice_drawing[num1]))
    print("\n".join(dice_drawing[num2]))
  else:
    quit()  

rollDice()    

