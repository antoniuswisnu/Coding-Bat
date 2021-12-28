def front3(str):
    if len(str) < 3:
        return str * 3
    else:
        return (str[0]+str[1]+str[2]) * 3
    


print(front3('aB'))