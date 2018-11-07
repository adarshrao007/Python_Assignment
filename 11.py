# Implement a program with functions, for finding the area of circle, triangle, square.

def circle(x):
	return (3.14*x*x);
def square(a):
	return (a*a);
def triangle(b,h):
	return (0.5*b*h);
x=int(input("enter radius of circle"))
a=int(input("enter radius of square"))
b=int(input("enter base of triangle"))
h=int(input("enter height of triangle"))

print("area of circle",circle(x))
print("area of square",square(a))
print("area of triangle",triangle(b,h))
