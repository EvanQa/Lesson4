#input age from user
# age: 10 11 12 -- print young
#       13 14 15 -- print teenager
#       16 17 18 -- print almost adult
#       19 20  -- print adult
#othewise -- print not in range

age: int = int(input('enter your age'))

#               #First way
# if age >= 10 and age <= 12:
#     print('young')
#
# elif age >= 13 and age <= 15:
#     print('teenager')
#
# elif age >= 16 and age <= 18:
#    print('almost adult')
#
# elif age >= 19 and age <= 20:
#    print('adult')
# else:
#     print('not in range')

            #Second way

if age in [10, 11, 12]:
    print('young')

elif age in [13, 14, 15]:
    print('teenager')

elif age in [16, 17, 18]:
    print('almost adult')

elif age in [19, 20]:
    print('adult')

else:
    print('not in range')

            #Third way
# match age:
#     case 10:
#         print('young')
#     case 11:
#         print('young')
#     case 12:
#         print('young')
#     case 13:
#         print('teenager')
#     case 14:
#         print('teenager')
#     case 15:
#         print('teenager')
#     case 16:
#         print('almost adult')
#     case 17:
#         print('almost adult')
#     case 18:
#         print('almost adult')
#     case 19:
#         print('adult')
#     case 20:
#         print('adult')
#     case _:
#         print('not in range ')

        #Fourth way
match age:
    case 10 | 11 | 12:
        print('young')
    case 13 | 14 | 15:
        print('teenager')
    case 16 | 17 | 18:
        print('almost adult')
    case 19 | 20:
        print('adult')
