print("_______Simple Function___________")
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()

#function that allows for input
print("____function that allows for input__________")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}")
greet_with_name("Rushikesh ")


print("______Function with more than two parameter________")

def greet_with(name,location):
    print(f"my name is {name}")
    print(f"My location is {location}")

greet_with("Rushikesh","Pune")
