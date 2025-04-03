####generator#####
###implimented during functions
###another way to cerate iterator
###uses keyword "yeild"
gen=(x for x in range (3))
print(gen)
for num in gen:
    print(num)
##################

gen=(x for x in range(3))
next(gen)

########################
gen=(x for x in range(3))
next(gen)
next(gen)

########################
#function which returns multiple values#
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

########instead of using for loop we can use our own generator####
gen=range_even(6)
next(gen)
next(gen)

####usecase: let us hide passward entered on screen
###chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
        
def hide(itr):
    for ele in itr:
        yield ele*'*'

passwards=["not-good","give'm-pass","00100=100"]
for passward in hide(lengths(passwards)):
    print(passward)
    
    
    
    
#############example1#####################
words = ["apple", "banana", "kiwi"]
for length in lengths(words):
    print(length)

##########################################
#enumerate
#printing lis with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1}{lst[index]}')
## same code using enumerate
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index}{item}')











