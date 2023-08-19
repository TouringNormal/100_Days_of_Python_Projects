print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))
total_bill = bill * ((tip / 100) + 1)
people_bill = total_bill / people
rounded_bill = "{:.2f}".format(people_bill)
print(f"Total for each person is {rounded_bill}$ per person")