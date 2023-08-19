height = input("what is your height in meters? ")
weight = input("What is your weight in kg? ")
bmi = float(weight) / (float(height) ** 2)
bmi_final = round(bmi)
if bmi_final < 18.5:
    print("You are underweight.")
elif bmi_final < 25:
    print("You are normal weight.")
elif bmi_final < 30:
    print("You are slightly overweight.")
elif bmi_final < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")