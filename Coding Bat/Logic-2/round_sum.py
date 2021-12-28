def round_sum(a, b, c):
    def round10(num):
        return round(num,-1)
    
    return round10(a)+round10(b)+round10(c)

print(round_sum(16,17,18))