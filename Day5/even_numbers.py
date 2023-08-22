total = 0
for number in range(2, 101, 2): # "2" in the end is the amount that is jumped like 2,4,6,8,10 etc.
    total += number
print(total)

#############
# another way to do this
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)