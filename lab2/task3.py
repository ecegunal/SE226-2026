# Task3
n = 0
while n < 3 or n > 9:
    n = int(input("Please enter a number between 3 and 9: "))
    if n < 3 or n > 9:
        print("Invalid number")

for i in range(1, 2 * n):

    ece = n - i
    if ece < 0:
        ece = -ece

    m = n - ece
    print("*" * m)
