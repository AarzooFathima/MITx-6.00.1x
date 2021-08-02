#An example for strings
x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + " . " + "x = " + x_str)

#example for while loop
n = 1
while n < 5:
    print(n)
    n = n + 1
    
#example for for loop
for n in range(5):
     print(n)

#break example
n = 0
for n in range(10):
    n = n + 1
    print(n)
    if n == 5:
        break

#range for computing mysum        
mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)
    
#Another example
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    print(mysum)

#range and break combo
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break 
print(mysum)


