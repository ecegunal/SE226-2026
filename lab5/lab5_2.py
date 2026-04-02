
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)



term = lambda x, i: (x ** i) / factorial(i)


def exp_x(x, n):
    total = 0
 
    for i in range(n):
        total = total + term(x, i)
    return total


x_degeri = float(input("enter x "))
n_degeri = int(input("enter n "))


sonuc = exp_x(x_degeri, n_degeri)
print("result", sonuc)
