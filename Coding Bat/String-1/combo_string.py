def combo_string(a, b):
    if len(a) < len(b):
        return a+b+a
    elif len(a) > len(b):
        return b+a+b

print(combo_string('Hello', 'hi'))