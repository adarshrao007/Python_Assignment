import re
email=input("Enter your email id:\n")
if re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email):
	print("VALID EMAIL ID")
else:
	print("INVALID EMAIL ID")