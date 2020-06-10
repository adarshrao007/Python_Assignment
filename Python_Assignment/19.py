import sys
import argparse
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a,b):
	return a*b
def division(a,b):
	return a/b
parser = argparse.ArgumentParser(description='CLA based calculator.')
parser.add_argument('-a', '--num1', type=int, required=True)
parser.add_argument('-b', '--num2', type=int, required=True)
parser.add_argument('--op','--operator', required=True)
args = parser.parse_args()
if(args.op == '+'):
    print( "\n Answer : ",add(args.num1 , args.num2))
    

elif(args.op == '-'):
    print( "\n Answer : ",subtract(args.num1 , args.num2))

elif(args.op == '*'):
    print( "\n Answer : ",multiply(args.num1 , args.num2))

elif(args.op == '/'):
    print( "\n Answer : ",division(args.num1 , args.num2))

else:
print("enter valid options")