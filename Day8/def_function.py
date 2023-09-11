def greet():
    print("Hello")
    print("There")
    print("Govna")
greet()

def greet_name(name): # "greet_name" is parameter, "name" is argument
    print(f"Hello {name}")
greet_name("Taavi")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"{location} seems like a nice place to live")

greet_with(location = "Tallinn", name = "Taavi")
