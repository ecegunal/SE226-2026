i = int(input("please enter large int "))

h = i // 3600

s = i % 3600

m = s // 60

seconds = s % 60

print(i, "seconds is", h, "hours,", m, "minutes, and", seconds, "seconds.")
