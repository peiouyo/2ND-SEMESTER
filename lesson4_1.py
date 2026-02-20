x = 300

print("Find the closest number to 300")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

diff_a = abs(x - a)
diff_b = abs(x - b)
diff_c = abs(x - c)

if a == b == c:
    print("All numbers are equal, therefore there is no number that is higher than the other.")
else:
    smallest = min(diff_a, diff_b, diff_c)

    if smallest == diff_a:
        print("The closest number to 300 is", a)
    elif smallest == diff_b:
        print("The closest number to 300 is", b)
    else:
        print("The closest number to 300 is", c)