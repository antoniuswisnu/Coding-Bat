def sum67(nums):
    count = 0
    blocked = False
    
    for i in nums:
        if i == 6:
            blocked = True
            continue
        if i == 7 and blocked:
            blocked = False
            continue
        if not blocked:
            count += i
            
    return count
    
print(sum67([1, 2, 2, 6, 99, 99, 7]))