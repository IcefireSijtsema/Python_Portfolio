def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print('{:^3} {:^10}'.format('C', 'F'))

    for celsius in range(-30, 41, 10):
        fahrenheit = convert(celsius)
        print('{:3} {:7}'.format(celsius, fahrenheit))
table()
