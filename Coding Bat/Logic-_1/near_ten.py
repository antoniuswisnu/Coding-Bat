def near_ten(num):
    a = num % 10
    if 0 <= a <= 2 or 8 <= a <= 9:
        return True
    else:
        return False
    
print(near_ten(19))