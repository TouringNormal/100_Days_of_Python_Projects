print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    age = int(input("What is your age? "))
    if age <= 18:
        bill = 7
        print("Your ticket price is 7$")
    elif age <= 12:
        bill = 5
        print("Your ticket price is 5$")
    elif age >= 45 and age <= 55: 
        print("Your ticket price is 0$")
    else:
        print("Your ticket price is 12$")
    photo = input("Would you like a picture as well? yes or no? ")
    if photo == "yes":
        bill += 3
    print(f"Your total bill is ${bill}")


    
else:
    print("Sorry, you're too short")