def end_other(a,b):
    if len(a) >= len(b):
        long,short = a,b 
    else:
        long,short = b,a
    return long.lower().endswith(short.lower())

print(end_other('HiAbc', 'abc'))