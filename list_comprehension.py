####list compression####
lst=[num for num in range(0,20)]
print(lst)

####capitalize in list compression###
name=['shraddha','chavan']
lst=[name.capitalize()for name in name]
print(lst)

#####list comprehension with if statement####
def is_even(num):
    return num%2==0
lst=[num for num in range(10)if is_even(num)]
print(lst)

####for loop in list comprehension####
lst=[f"{x}{y}" for x in range(3)for y in range(3)]
print(lst)

####set comprehension###
set_one={x for x in range(3)}
print(set_one)

####dictionary comprehension#####
dict={x:x*x for x in range(3)}
print(dict)

#sqaure of a number:
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

#even numbers:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8]

#uppercase letters
words = ["apple", "banana", "cherry"]
uppercased = [word.upper() for word in words]
print(uppercased)
# Output: ['APPLE', 'BANANA', 'CHERRY']


#transforming image pixel
pixels = [100, 150, 200, 250]
adjusted = [min(255, pixel + 50) for pixel in pixels]  # Ensure max pixel value is 255
print(adjusted)
# Output: [150, 200, 250, 255]







