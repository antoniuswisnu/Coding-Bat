def centered_average(nums):
    data = []
    for i in range(1,len(nums)+1):
        data.append(i) 
    mean = (data[0] + data[-1]) // 2
    print(mean)
    print(data)
    if len(data) % 2 != 0:
        return nums[mean-1]
    else:
        return (nums[mean] + nums[mean-1]) // 2
        
print(centered_average([-10, -4, -2, -4, -2, 0]))