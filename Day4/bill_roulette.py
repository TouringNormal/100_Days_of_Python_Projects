import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_amount = len(names)

bill = random.randint(0, names_amount -1) # "-1" is because "0" is the start and the list length is added but then it would be too long by one
pays = names[bill]

print(f"{pays} is going to pay the bill")