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
