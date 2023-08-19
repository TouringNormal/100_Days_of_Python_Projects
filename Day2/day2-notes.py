#String
print("Hello"[4]) #[4] determine which letter is shown in the output

# Integer
123_456_789 # "_" is like a comma separator for easier readability

#Float
3.14

#Boolean
True
False

################################

print(type("some kind of data")) # Tells what type of data is in the brackets
a = float(123) # turns a integer into float

################################

3 ** 3 # "**" is power so the anwser is 27 as in 3*3*3

8 // 3 # "//" turns comma  into a full number so it'll be an int instead of float

score = 0
score += 1 # this adds 1 to the score parameter

############################################
score = 0 # integer
height = 10.00 # Float
isWinning = True # Boolean
#f-String makes all different data into one string
print(f" your score ise {score}, height is {height}, you are winning {isWinning}")

rounded_bill = "{:.2f}".format(33.6)
# result is 33.60
# '"{:.2f}".format' is a way to round numbers into a way that even 0 is displayed