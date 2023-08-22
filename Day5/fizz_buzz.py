for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        numbers = "Fizzbuzz"    
    elif numbers % 3 == 0:
        numbers = "Fizz"
    elif numbers % 5 == 0:
        numbers = "Buzz"
    
    print(numbers)

