#Task 1
n = int(input("please enter a value which is bigger than 1"))
size = 0
print(n, end="")

while n > 1:
    if n % 2 == 0:
        n = n // 2
      
    else:
       n = (n * 3) + 1
    print(" →", n, end="")
    size = size + 1
print()
print("Total steps:", size)
