#     Consider an array/list of sheep where some sheep may be missing from their place.
#     We need a function that counts the number of sheep present in the array (true means present).
#     For example,
#
#     [True,  True,  True,  False,
#       True,  True,  True,  True ,
#       True,  False, True,  False,
#       True,  False, False, True ,
#       True,  True,  True,  True ,
#       False, False, True,  True]

#     The correct answer would be 17.

# Solution 1

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

array = [
    True, True, True, False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
    ]

print(count_sheeps(array))

# Solution 2

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

# Solution 3

def count_sheeps(sheep):
    return sheep.count(True)

# Solution 4

count_sheeps = lambda x: x.count(1)