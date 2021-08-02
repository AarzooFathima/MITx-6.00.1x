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
