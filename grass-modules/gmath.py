def add(type, a, b):
    if type == 'Str':
        print(a + b)
    elif type == 'Int':
        try:
            print(int(a) + int(b))
        except ValueError as VE:
            print('Error:', VE)
    elif type == 'Float':
        try:
            print(float(a) + float(b))
        except ValueError as VE:
            print('Error:', VE)
    else:
        print('Invalid Value for Type: %s' % type)

def mod(type, a, b):
    if type == 'Str':
        print(a % b)
    elif type == 'Int':
        try:
            print(int(a) % int(b))
        except ValueError as VE:
            print('Error:', VE)
    elif type == 'Float':
        try:
            print(float(a) % float(b))
        except ValueError as VE:
            print('Error:', VE)
    else:
        print('Invalid Value for Type: %s' % type)
