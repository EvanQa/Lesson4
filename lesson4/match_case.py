# input a number from the user
#if number is 1 ==> print('Sunday')
#               ==> print('Monday')
#                ..
#             7 ==> print('Saturday')
#otherwise print('invalid day number')

day: int = int(input('Enter a number'))

#if x is 1:  another way instead of '=='
if day == 1:
    print('Sunday')
elif day == 2:
    print('Monday')
elif day == 3:
    print('Tuesday')
elif day == 4:
    print('Wensday')
elif day == 5:
    print('Thursday')
elif day == 6:
    print('Friday')
elif day == 7:
    print('Saturday')
else:
    print('invalid day number')

#short way

match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wensday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('invalid day number')