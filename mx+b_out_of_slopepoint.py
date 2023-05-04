m = float(input("Slope? "))
x = float(input("X? "))
y = float(input("Y? "))

n = m*x
b = y-n

if b >= 0:
    op = str("+")
elif b < 0:
    op = str("")


print("Y=" + str(m) + "x" + str(op) + str(b))