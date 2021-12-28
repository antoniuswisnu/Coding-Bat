def cat_dog(str):
    for i in range(len(str)-1):
        if i + [i+1] + [i+2] == "cat" and i + [i+1] + [i+2] == "dog" :
            return True
        else:
            return False
        
print(cat_dog('catdog'))

