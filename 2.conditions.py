n = int(input("Input a number: "))

if n < 0:
    print(f"{n} is a negative number")
elif n > 0:
    print(f"{n} is a positive number")
else:
    print(f"{n} is zero")