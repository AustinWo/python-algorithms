input = [5,4,3,2,1,1,2,3,4,5,6,7]

def bubbleSort(nums):
    for x in range (0, len(nums)-1):
        for y in range (x+1, len(nums)):
            if (nums[x] > nums[y]):
                nums[x], nums[y] = nums[y], nums[x]
    return nums

print(bubbleSort(input))