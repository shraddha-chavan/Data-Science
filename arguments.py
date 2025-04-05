#1.positional arguments 
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Shraddha", 20)  # name = "Shraddha", age = 25

#2. default arguments 
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("Shraddha")       # age = 18 (default)
greet("Omkar", 10)   # age = 30 (overrides default)

#3. arbitrary positional(*args) argument
def add_numbers(*numbers):
    total = sum(numbers)
    print("Sum is:", total)

add_numbers(1, 2, 3)
add_numbers(5, 10, 15, 20)

#4. arbitrary keyword (**kwargs) argument
def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe_person(name="Shraddha", age=20, city="Kopergaon")
