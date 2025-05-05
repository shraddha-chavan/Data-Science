# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:12:41 2025

@author: Latitude 5410
"""
######################################################
x=1000000000000000000000000000000000
print(x)
print(type(x))
x=1
print(x)
print(type(x))

age=input("enter your age:")
print(type(age))
print(age)
age1=input("enter your age:")
print(type(age1))
print(age1)
age=age+age1
print(age)
age2=input("enter your age:")
print(type(age2))
print(age2)
age2=input(age2)
print(type(age2))
age=age1+age2
print(age)


age=float(input("enter your age:"))
print(type(age))
print(age)

int_value=100
string_value='1.5'
float_value=float(int_value)
print('int value in float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value in float:',float_value)
print(type(float_value))
#complex numbers
c1=1
c2=2j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c1.imag)
#######################################################################
#Boolean
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

status=bool(input('ok it is confirmed'))
print(status)
print(type(status))
################################################################
#arithmetic operation
home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goal_for=10
goal_against=7
print(goal_for - goal_against)
print(type(goal_for - goal_against))

print(100/20)
print(type(100/20))

#global variable
x="awesome"
def my_function():
    print("python is "+x)
my_function

#global and local varaible 
x="awesome"
def my_function():
    x="fantastic"
    print("python is"+x)
my_function
print("python is "+x)

########
x=range(8)
print(x)
print(type(x))

########dictionary#######
x={"name":'ram',"age":12}
print(type(x))

########type casting######
x=int(1.4)
print(x)
x=1
z=float(x)
print(z)

####string concatenation####
str1="hello"
str2=2
str3=str1+str2
print(f"hello{str2}")

##if you want multiple strings##
x="""my name is shraddha.from ece"""
print(x)

###string slicing###
x="""mynameis shraddha.from ece"""
print(x[2:8])

#####slice from start####
x="I am studing in jay colonay"
print(x[:16])

####slicing from end####
x="""my name is shraddha.from ece"""
print(x[7:])

####negative indexing###
x="""my name is shraddha.from ece"""
print(x[-5:-2])

###modify string
print(x.upper())

###upper /lower###
x=x.upper()
print(x.lower())

###remove white space =use strip function
x="""my name is shraddha.from ece"""
print(x.strip())

####for right hand side strip###
x="this is python"
print(x.rstrip())
x="Hello world"
print(x.replace("Hello ","world"))

####use of split whic replace white space###
x="Hello world"
print(x.split(" "))

x='green-red-blue'
print(x.split('-'))

x='''my name is shraddha.from ece'''
print(x.split('.'))

####assignment1###
x='''red-green-blue-yellow'''
def sorted_colors(x):
    
sorted_alphabetic=sorted_colors(x)
print(sorted_alphabetic)


##Q.2. Write program to write prime numbers between 10 to 99.

for num in range(10, 100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
    


####Q1 Print from 23 to 58 ######

for number in range(23, 58):
    if number % 2 == 0:
       print(number)
 
    
 ###Q3 Palidrome #####
 
def is_palindrome(n):
     return str(n) == str(n)[::-1]

     num=121
     if is_palindrome(num):
         print({num},"Number is palindrome")
     else:
         print({num},"Number is not palindrome")
    
 
car={'name':'shraddha','age':12}
print(car.get('age'))
    
 #sorting for min values in dict
sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}    
free_items_key = min(sorted_dict,key=sorted_dict.get) 
free_items_value = sorted_dict[free_items_key]   
print(f"you will get the lowest item'{free_items_key}'('{free_items_value}'")
    
#min(my_dict):returns the min key.
#min(my_dict.values()) :returns min value
#min(my_dict,key=my_dict.get):returns the key corresponding to min value
    
 #sorting for max values in dict
sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}    
free_items_key = max(sorted_dict,key=sorted_dict.get) 
free_items_value = sorted_dict[free_items_key]   
print(f"you will get the lowest item'{free_items_key}'('{free_items_value}'")
    

    
#sorting in descending order
sorted_by_values_desc=dict(sorted_dict.items(),key=lambda item:items)
print(sorted_by_values_desc)
    
 #adding values of dict
dict1={'banana':40,'apple':100,'grapes':120,'mango':200} 
sum=0
for value in dict1.values():
    sum=sum+int(value)
print(sum)
   
 #convert values to integers and sum them up
dict1={'banana':40,'apple':100,'grapes':120,'mango':200} 
total_sum = sum(int(value) for value in dict1.values())
print(total_sum)
    
#concatenation of dict
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
print(dict1)
dict1.update(dict3)
print(dict1)
#another way to concatenate
dict1=dict1|dict2|dict3
print(dict1)


#write a program to check wheather the element is in dict or not
dict1={'a':2,'b':3}
print('a' in dict1)

#whie loop
i=1
while i < 6:
    print(i)
    i=i+1
#with break statement we can stop the loop even if the while loop 
i=1
while i < 6:
    print(i)
    if(i==3):
      break
    i=i+1

#h.w
#suppose u r selling milk 10 liters, and there is queue of customers
#the movement sell reaches to 100 liters, u need to inform the coustomer
#that the milk finished
def sell_milk():
    total_sold = 0
    while total_sold < 100:
        sold = int(input("Enter liters of milk sold: "))
        total_sold += sold
        if total_sold >= 100:
            print("The milk has finished.")
            break
        else:
            print(f"Milk sold so far: {total_sold} liters")

if __name__ == "__main__":
    sell_milk()








#continue to the next iteration if i is 3
i=1
while i < 6:
    i=i+1
    if(i==3):
       continue
    print(i)

#h.w
#suppose u r standing in queue to audi , where students and professers r in queue , 
#if the professer r there u r allowing without checking ;
#but if there is syudent the he/she will be checked

def check_queue(queue):
    for person in queue:
        if person == "Professor":
            print(f"{person}: Allowed without checking.")
        else:
            print(f"{person}: Checked.")

if __name__ == "__main__":
    queue = ["Professor", "Student", "Professor", "Student", "Professor"]
    check_queue(queue)



#for loop
dict={"apple","banana","cherry"}
for i in dict:
    print(i)

#for loop for break
dict={"apple","banana","cherry"}
for i in dict:
    if i=="banana":
        break
    print(i)

#for loop for continue 
dict={"apple","banana","cherry"}
for i in dict:
    if i=="banana":
        continue
    print(i)
#the range function returns a sequence of no.
for x in range(6):
    print(x)
###############
for x in range(2,30,3):
    print(x)

###loop inside loop
colors={"green","yellow","blue"}
fruits={"apple","banana","cherry"}
for x in colors:
    for y in fruits:
        print(x,y)


#for checking odd or even no.
#for negative no. for checking even or odd no.
num= int(input("Enter a number:"))
if num<0:
    print("negative no.",num%2==0)


#function without arguement
def my_function():
    print("hello from a function")

#function with arguement
def my_function(name):
    print("Hello", " " +name)
my_function("Shraddha")    

#function with postional arguement
def my_function(name2,name1):
    print(name1+" "+name2)
my_function("World","Hello")    

#Arbitary arguement,"args"
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("shraddha","tanuja","chanchal")

#exclusive for dict
#we use name kwargs with double stars the reason is that the double stars allows us to pass through keyword arguement 
#a keyword arguement is whwere u provide a name to the variable as u pass alongside it
#that is why when we iterate it iver the kwargs
#there dosent seem to be any order
#in which they were printed out

def myFun(**kwargs):
    for key,value in kwargs.items():
        #print(%s==%s%(key,value))
        print(f'{key}:{value}')
myFun(first_name='shraddha',mid_name='sunil',last_name='chavan')



#if we call the func without arguement
#it uses the default value
def myFun(country="Norway"):
    print("I am from" + country)
my_function('dubai')    
my_function('sweden')    
my_function('india')    
my_function()    
my_function('brazil')    

#if u send a list as a arguement , it will still be a list
fruits=["orange","apple","cherry"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)

# returns value
#to let a function return a value , use the return statement
def my_function(x):
    y=x*5
    return y
my_function(5)

#if in a func we have 2 values it will be in tuples format
def my_function(x):
     y=x*5
     z=x*7
     return y,z
my_function(5)



#pass function
def my_function():
    pass
my_function()
    
#recursive func
def factorial(x):
    if x==1:
        return
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

###lambda func
def add(a):
    sum=a+10

    return sum
add(20)
add=lambda a:a+10
print(add(20))

#lambda function can take any no. of arguemennt
add=lambda a,b:a+b
print(add(5,6))

#filter function for odd no.
lst=[12,33,22,55,66]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)

#filter function for even no.
lst=[12,33,22,55,66]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

#map func for finding square root
lst=[12,33,22,55,66]
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)

#split()
text="apple,banana,orange"
words=text.split(" ,")#split by comma
print(words)

#join()
new_text="-".join(words)
print(new_text)

#find(),index()
text="Hello Python !"
print(text.find("Python"))
print(text.find("Java"))
print(text.index("Python"))
print(text.index("Java"))


#count()
text="apple,banana,orange"
print(text.count("banana"))

#startswith(),endswith()
text="My name is shraddha"
print(text.startswith("My"))
print(text.endswith("shraddha"))


# isalpha(),isdigit(),isalnum()
text="Shraddha123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

text="ShraddhaChavan"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

#issupper(),islower()
text1="HELLO"
text2="Hello123"
text3="12345"
count1=0
for i in range(len(text1)):
    if text1[i].isupper():
        count1=count1+1 
print(count1)

#islower()
text1="HELLO"
text2="Hello123"
text3="12345"
count1=0
for i in range(len(text2)):
    if text2[i].islower():
        count1=count1+1 
print(count1)

#Does full stop is in endswith 
str="There are no traffic jams along extra mile."
ans=str.endswith(".")
print(ans)

#pyramids(mario)
for i in range(1,6):
    for j in range(1,i+1):
        print("#",end="  ")
    print()    
######################
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="  ")
    print()    

########################
for i in range(6):
    for j in range(6-i):
        print("#",end="  ")
    print()    

########################
for i in range(4):
    for j in range(4):
        print("#",end="  ")
    print()    

#######################
#finding missing number 
def missing_num(lst,n):
    expected_num=n*(n+1)//2
    actual_num=sum(lst)
    missing_num=expected_num-actual_num
    return missing_num
lst=[1,2,4,5,6]
n=6#including missing number
print("Missing number:",missing_num(lst,n))


#reverse a string without built in function
def rev_string(s):
    rev_s=s[::-1]
    return rev_s
s="My name is shraddha"
rev_s=rev_string(s)
print(rev_s)

#in one line reverse string
rev_string=input("Enter the string:")[::-1]
print(rev_string)

#write a program to check wheather vowels are present in a sentence
char=input("Enter a string:").lower()

if any (vowel in char for vowel in"aeiou"):
    
    print("Vowels are present in sentence")
else:
    print("Vowels are not present in sentence")
    











