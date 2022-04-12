# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.

# Solution 1
# Let's use reducemethod to solve this task.
# It executes a reducer function (that you provide) on each element of the array,
# resulting in single output value. It is almost a textbook example for reducer.

import functools
def positive_sum(arr):
    return functools.reduce(lambda accumulator, current: accumulator + (current if current > 0 else 0), arr, 0)

# Solution 2
# Another approach will be to loop over the array and sum all positive numbers.

def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
    return sum

# Solution 3
# Or to use sum(). This is an inbuilt function in python that adds
# all the elements in list, set and tuples and returns the value.

def positive_sum(arr):
    return sum(number for number in arr if number > 0)

# Solution 4

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# Solution 5

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))