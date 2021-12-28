def cigar_party(cigars, is_weekend):
    if 40 <= cigars <= 60 and is_weekend == False:
        return True
    elif 40 <= cigars and is_weekend == True:
        return True
    else:
        return False

print(cigar_party(70, True))