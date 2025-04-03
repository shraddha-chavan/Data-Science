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
















