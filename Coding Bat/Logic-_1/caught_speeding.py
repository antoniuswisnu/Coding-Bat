def caught_speeding(speed, is_birthday):
    if is_birthday == False:
        if 60 >= speed:
            return 0
        elif 60 < speed <= 80:
            return 1
        elif 81 <= speed:
            return 2
    elif is_birthday == True:
        if 65 >= speed:
            return 0
        elif 65 < speed <= 85:
            return 1
        elif 85 < speed:
            return 2

print(caught_speeding(79, True))