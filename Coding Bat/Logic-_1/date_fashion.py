def date_fashion(you, date):
    if 0 <= you <= 10 and 0 <= date <= 10:
        if you <= 2 or date <= 2:
            return 0
        elif you >= 8 or date >= 8:
            return 2
        else:
            return 1
    
print(date_fashion(5, 10))