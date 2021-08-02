#square root
x = int(input('Enter an integer: '))
ans = 0
while ans**2 < x:
    ans = ans + 1
if ans**2 != x:
    print(str(x) + ' is not a perfect square')
else:
   if x < 0:
        ans = - ans
    print('Square root of ' + str(x) + ' is ' + str(ans))

    
#cube root
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
   if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))

    
