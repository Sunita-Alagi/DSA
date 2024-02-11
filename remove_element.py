# return true if array can be made strictly increasing after removing exactly one element,
# or false otherwise. If the array is already strictly increasing, return true.

# The array nums is strictly increasing if nums[i - 1] < nums[i] 
# for each index (1 <= i < nums.length).

# Input: nums = [1,2,10,5,7]
# Output: true


def can_be_increaseing(nums):
    temp = nums
    count_remove = 0
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1]:
            continue
        elif count_remove == 0 :
            temp.remove(nums[i])
            count_remove += 1
    if temp == sorted(temp):
        return True
    else:
        return False

               
nums = [1,2,10,5,7]
# nums = [2,3,1,2]
print(can_be_increaseing(nums))