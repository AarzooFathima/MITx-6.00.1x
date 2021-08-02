#1. Convert the following into code that uses a while loop.
"""
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
num = 0
while True:
    num += 2
    if num <= 10:
        print(num)
    else:
        print("Goodbye!")
        break

#2. Convert the following into code that uses a while loop.
"""
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
print("Hello!")
num = 10
while num != 0:
    print(num)
    num = num - 2
    
#3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, 
#your code should print out the result:21, which is 1 + 2 + 3 + 4 + 5 + 6.
#end = 6
i = 1
num = 0
while i <= end:
    num = num + i
    i = i+1
print(num)
    

    
