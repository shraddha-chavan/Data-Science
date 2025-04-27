
#opening a file
file = open("example.txt", "r")  # "r" means read mode

#reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
##############################################################################
#user login system::
# Step 1: Take input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Step 2: Write the data to a file
with open("user_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("Data saved successfully!\n")

# Step 3: Read and display the data from the file
with open("user_data.txt", "r") as file:
    print("Reading data from file:")
    print(file.read())
#########################################################################################
#usecase:student registration
# Function to register a new student (write to file)
def register_student(name):
    with open("students.txt", "a") as file:
        file.write(name + "\n")
    print(f"Student '{name}' registered successfully!")

# Function to show all registered students (read from file)
def show_all_students():
    print("Registered Students:")
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())

# Example usage
register_student("Alice")
register_student("Bob")
register_student("Charlie")

show_all_students()
