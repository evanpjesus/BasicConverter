import math

print('Welcome to Unit Converter!')
print('We support the following conversions:')
print('Miles /n Kilometers /n Pounds /n Kilograms')
convertThis = input('What do you want to input, followed by the unit :')

converting2 = convertThis[-2:]
amount2 = convertThis[:-3]

print(converting2)
print(amount2)

def identify():
    if 'km' in converting2.lower():
        print(amount2, converting2, '1')

    elif 'm' in converting2.lower():
        print(amount2, converting2, '2')
    elif 'lb' in converting2.lower():
        print(amount2, converting2, '3')
    elif 'kg' in converting2.lower():
        print(amount2, converting2, '4')
    else:
        print('Hmmm...Maybe try using these. /n lb(Pounds), kg(Kilogram), mi(miles/miles per hour), km(kilometers)')
        identify()
