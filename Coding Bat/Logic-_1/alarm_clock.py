def alarm_clock(day, vacation):
    for i in range(1,6):
        if vacation == False:
            if day == i:
                return '7:00'
            elif day == 6 or day == 0:
                return '10:00'
        elif vacation == True:
            if day == i:
                return '10:00'
            elif day == 6 or day == 0:
                return "off"

print(alarm_clock(0, True))
