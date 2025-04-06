
#opening a file
file = open("example.txt", "r")  # "r" means read mode

#reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
