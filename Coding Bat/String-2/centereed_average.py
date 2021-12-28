def centered_average(nums):
    x = 0
    for i in range(len(nums)):
        x = i + 0
    y = x + 1
    if y % 2 == 0:
        return (nums[y/2] + nums[(y/2)+1]) /2
    else:
        return nums[y/2]

print(centered_average([1, 2, 3, 4, 100 ]))