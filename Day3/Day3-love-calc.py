print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1.lower() + name2.lower()


t = int(name.count('t'))
r = int(name.count('r'))
u = int(name.count('u'))
e = int(name.count('e'))
l = int(name.count('l'))
o = int(name.count('o'))
v = int(name.count('v'))
name_total_true = t + r + u + e
name_total_love = l + o + v + e

print(name_total_true, name_total_love)
total = int(str(name_total_true) + str(name_total_love))


if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
