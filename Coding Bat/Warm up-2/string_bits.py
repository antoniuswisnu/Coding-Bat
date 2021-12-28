def string_bits(str):
    hasil = ""
    for i in range(len(str)):
        if i % 2 == 0:
            hasil += str[i]
    return hasil

print(string_bits('Heeololeo'))