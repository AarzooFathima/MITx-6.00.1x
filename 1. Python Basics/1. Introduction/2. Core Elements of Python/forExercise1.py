#1. Convert the following code into code that uses a for loop.
"""
prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
for i in range(2,13,2):
    if i <= 10:
        print(i)
    else:
        print("Goodbye!")
        break
