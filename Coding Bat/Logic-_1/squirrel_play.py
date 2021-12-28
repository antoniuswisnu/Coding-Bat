def squirrel_play(temp, is_summer):
    if 60 <= temp <= 90:
        return True
    elif is_summer == True:
        if 90 < temp <= 100:
            return True
        else:
            return False
    else:
        return False
    
        
print(squirrel_play(50, False))