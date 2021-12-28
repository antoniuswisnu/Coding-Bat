def in1to10(n, outside_mode):
    if outside_mode == False:
        if 0 < n < 11:
            return True
        else:
            return False
    elif outside_mode == True:
        if n <= 1 or n >= 10:
            return True
        else:
            return False

print(in1to10(9, True))
