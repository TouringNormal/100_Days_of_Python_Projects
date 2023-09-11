programming_dictionary = { #{Key: Value}
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

#Adding new keys to the dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Creating an empty dictionary
empty_dictionary = {}

#Wiping an existing dictionary
'''programming_dictionary = {}
print(programming_dictionary)'''

#Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Looping through a dictionary
for key in programming_dictionary:
    print(key) #This gives only the Keys
    print(programming_dictionary[key]) #This gives the Key value

#Nesting the dictionary
capitals ={
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Hannover"],
}

#Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Hannover"], "total_visits": 7},
}

#Nesting dictionaries in a List

travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited":["Berlin", "Hamburg", "Hannover"], 
        "total_visits": 7
    },
]