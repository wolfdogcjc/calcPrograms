def calc_slope_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return (m, b)


x1 = float(input("X1=? "))
y1 = float(input("Y1=? "))
x2 = float(input("X2=? "))
y2 = float(input("Y2=? "))

m, b = calc_slope_intercept(x1, y1, x2, y2)

print("The equation of the line is: y = {:.2f}x + {:.2f}".format(m, b))

