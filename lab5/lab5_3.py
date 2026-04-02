
total_sum = 0.0


def hesapla(n):

    global total_sum

    if n == 0:
        return

    hesapla(n - 1)
    terim = ((-1) ** (n + 1)) / n


    total_sum = total_sum + terim


ndegeri = int(input("enter n "))

hesapla(ndegeri)

print("result", total_sum)
