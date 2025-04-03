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


