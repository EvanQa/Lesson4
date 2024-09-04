# we require to be bigger than 18 y.o
#and more than 10000 in balance

                                 #firs way
# True and True => True
# True and False => False
# False and True => False
# False and False => False
age: int = int(input("what is your age?"))
balance: int = int(input("what is your balance?"))

if age > 18 and balance > 100000:
    print('you are qualified for the program')
else:
    print('you are NOT qualified for the program')


                            #second way
# True or True => True
# True or False => True
# False or True => True
# False or False => False
if age <= 18 or balance <= 100000:
    print('you are qualified for the program')
else:
    print('you are NOT qualified for the program')


                            #third way
if age > 18 and not balance <= 100000:
    print('you are qualified for the program')
else:
    print('you are NOT qualified for the program')

