# Task2
n = 0
while n < 10 or n > 100:
    n = int(input("Please enter a number between 10 and 100: "))
    if n < 10 or n > 100:
        print("Invalid input. Please enter a number between 10 and 100: ")

fiz = 0
buz = 0
fizbuz = 0

for i in range(1, n + 1):

    if i % 7 == 0:
        print("(", i, "is skipped )")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizbuz = fizbuz + 1


    elif i % 3 == 0:
        print("Fizz")
        fiz = fiz + 1


    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
        buz = buz + 1


    else:
        print(i)


print("--- Summary ---")
print("Fizz count :", fiz)
print("Buzz count :", buz)
print("FizzBuzz count:", fizbuz)
