import random


ask = input("What do you choose? 0 for rock, 1 for paper, 2 for scissors: ")

options = ["Rock", "Paper", "Scissors"]

choice = int(ask)
if choice >= 3 or choice < 0:
    print("Please choose a right number")
else:
    human = options[choice]
    ai = random.randint(0, 2) 
    ai_choice = options[ai]

    if choice == ai:
        print (f"You chose {human}, AI chose {ai_choice}. It's a draw")
    elif choice == 0 and ai == 1:
        print (f"You chose {human}, AI chose {ai_choice}. You lost")
    elif choice == 1 and ai == 2:
        print (f"You chose {human}, AI chose {ai_choice}. You lost")
    elif choice == 0 and ai == 2:
        print (f"You chose {human}, AI chose {ai_choice}. You won")
    elif choice == 2 and ai== 1:
        print (f"You chose {human}, AI chose {ai_choice}. You won")
    elif choice == 2 and ai== 0:
        print (f"You chose {human}, AI chose {ai_choice}. You lost")
    elif choice == 1 and ai== 0:
        print (f"You chose {human}, AI chose {ai_choice}. You won")
