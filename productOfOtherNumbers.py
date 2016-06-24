# do not use division

input = [1,2,6,5,9]

def productOfOtherNumbers(ints):
    result = []
    for x in range(0, len(ints)):
        # we will use x as the index of the result element
        total = 1

        # multiply all the ints but skip the current index
        for y in range(0, len(ints)):
            if x == y:
                continue
            total *= ints[y]

        result.append(total)

    return result

# print(productOfOtherNumbers(input))

# time complexity: o(n^2)
# space complexity: o(n):


# ======================================================================

def productOfOtherNumbersLinear(ints):
    result = []
    soFar = 1
    for i in range(0, len(ints)):
        # calculate sum of previous ints
        result.append(soFar)
        soFar *= ints[i]


    soFar = 1
    for x in range(len(ints)-1, -1, -1):
        result[x] *= soFar
        soFar *= ints[x]

    return result

print(productOfOtherNumbersLinear(input))

# time complexity: o(n)
# space complexity: o(n)