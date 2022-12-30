def first_last6(nums):
    count = len(nums)
    if(nums[0]==6 or nums[len(nums)-1]==6):
        return True
    else:
        return False

print(first_last6([1,3,4,6]))            