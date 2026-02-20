print("Find the largest number among three numbers")

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if a >= b and a >= c:
    print(f"The first number is the largest value with a value of {a}")
elif b >= a and b >= c:
    print(f"The second number is the largest value with a value of {b}")
else:
    print(f"The third number is the largest value with a value of {c}")