nums = [0,1,2,3,4,5]

from random import randint

def shuffle(vals):
    i = len(vals)-1
    while i > 0:
        randomI = randint(0,i-1)
        # swap the values
        vals[randomI], vals[i] = vals[i], vals[randomI]
        i -= 1
    return vals

print(shuffle(nums))

""" 

time complexity: o(n)
space complexity: o(1)

Common mistakes: 

1) pointer to an element in a list is read only
val = nums[0] -> 0
val = 5
print(nums[9]) -> still 0 
print(val) -> 5

2) infinite loop

3) index error

4) forget to return


lessons:

1) from random inport randint
2) randomize ints in range including start and end: randint(start, end)

"""