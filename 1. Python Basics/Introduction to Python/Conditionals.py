#A SIMPLE EXAMPLE
x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')

#NESTED CONDITIONALS
x = int(input('Enter an integer: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

# COMPOUND BOOLEANS
x = int(input('Enter an integer: '))
y = int(input('Enter an integer: '))
z = int(input('Enter an integer: '))
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least') 
