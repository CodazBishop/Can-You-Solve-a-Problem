
#python program to solve the quadratic equation ax^2 + bx + c = 0
import cmath

a = int(input("enter a number here:"))
b = int(input("enter a number here:"))
c = int(input("enter a number here:"))


d = (b**2) - (4*a*c)


x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(x1,x2))
