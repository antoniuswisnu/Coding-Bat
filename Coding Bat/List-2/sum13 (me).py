def sum13(nums):
    data = []
    for i in nums:
        data.append(i)
    hasil = []
    for j in range(len(data)):
        if data[j] == 13:
            pass
        else:
            hasil.append(data[j])
    return sum(hasil)
        
        
print(sum13([1, 1]))