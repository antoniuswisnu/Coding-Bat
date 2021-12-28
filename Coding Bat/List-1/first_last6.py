def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

print(first_last6([7, 6, 2, 3])) 