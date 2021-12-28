def sleep_in(weekday, vacation):
    if weekday == True and vacation == True:
        return True
    elif weekday == False or vacation == True:
        return True
    else:
        return False

print(sleep_in(False,True))