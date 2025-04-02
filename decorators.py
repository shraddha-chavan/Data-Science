#######pre- requisite to decorator######
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)


#######defing function inside function######
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)


#####passing function as arguements
#to other functions
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

##function returning function###
def hello_function():
    def say_hi():
        return"HI SHRADDHA"
    return say_hi
hello=hello_function()
hello()
##function returning function gives object##


##Need for decorators
import time
def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution square is {total_time}")
    return result


def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution cube is {total_time}")
    return result
array=range(1,1000)
out_square = calc_square(array)
out_cube = calc_cube(array)
   

###uppercase_decorator#####
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func =function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate()

###python provides a much easier way 
#for us to apply decorators
#we simply use @ symbol before
# the function we like to decorate

def uppercase_decorator(function):
    def wrapper():
        func =function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()


###split string and uppercase#################
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
def uppercases_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper


@split_string
@uppercase_decorator
def say_hi():
    return'hello there'

say_hi()

#############decorator for squares and cubes#############
import time
def time_it(func):
    
    #this is a decorator function 
    #that take another functiom
    def wrapper(*args,**kwargs):
        #*args and ** kwargs allows wrapper
        #to accept any number of 
        #positional and keyword
        start=time.time()
        result=func(*args,**kwargs)
        #calls the original function(func)
        #with the provided arguements
        end=time.time()
        print(func.__name__+'took'+str((end-start)*1000)+ ' mili second')
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result


@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,100000)
out_square= calc_square(array)
out_square= calc_cube(array)



#automatically logs function calls and their arguements
def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Calling{func.__name__}with {args}{kwargs}")
        return func(*args,**kwargs)
    return wrapper
@log_decorator
def add(a,b):
    return a+b

print(add(3,4))#logs the function call

#Access control/ Authentication
#check if a user is authenticated 
#before executing a function

def auth_required(func):
    def wrapper(user):
        if not user.get("authenticated",False):
            #the .get("authenticated",false)method 
            #is used to safely retreive the value of the 
            # authenticated key from the dictionary
            
            print("Access Denied")
            return
        return func(user)
    return wrapper
            
@auth_required
def dashboard(user):
    print(f"Welcome, {user['name']}!")
    
# Test cases
user1=({"name": "Alice", "authenticated": True})  # Output: Welcome, Alice!
user2=({"name": "Bob", "authenticated": False})   # Output: Access Denied           
            
dashboard(user1) #access granted       
dashboard(user2)   #access denied  
          
            





