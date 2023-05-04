# Python program to find roots of quadratic equation
import math


# function for finding roots
def equationroots( a, b, c):

	# calculating discriminant using formula
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))
	
	# checking condition for discriminant
	if dis > 0:
		print(" real and different roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	
	elif dis == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	
	# when discriminant is less than 0
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)

# Driver Program
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


# If a is 0, then incorrect equation
if a == 0:
		print("Input correct quadratic equation")

else:
	equationroots(a, b, c)

#   5x^2 + 26x + 5
#      (5x+1) (x+5)
#    r1 = -.2      r2= -5
#   0 = (k*-.2 + h)