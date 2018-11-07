#Implement a calculator program for above using getopt.

import sys
import getopt

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a,b):
	return a*b
def division(a,b):
	return a/b
	
opts,args=getopt.getopt(sys.argv[1:],"a:o:b:",["num1=","operator=","num2="])
for key,value in opts:
	if (key=='-a' or key=='--num1'):
		num1=int(value)
		print("first number is:",num1)                                                               
	elif(key=='-o' or key=='--operator'):
		operator=value
		print("entered operator is :",operator)
	elif(key=='-b' or key=='--num2'):
		num2=int(value)
		print("second number is:",num2)
	else:
		sys.exit();

if num1 and num2 and operator:
	if(operator=='+'):
		print("addition:",add(num1,num2))
	elif(operator=='-'):
		print("sub:",subtract(num1,num2))
	elif(operator=='*'):
		print("mul:",multiply(num1,num2))
	elif(operator=='/'):
		print("div:",division(num1,num2))
	else:
		print("enter valid operator")
