import re
username=input('enter the username\n')
ulen=len(username)
if(ulen<10):
	print("IT IS VALID USERNAME")
	
else:
	print("<INVALID USERNAME>----Username must not exceed 10 characters")

	

password=input("enter the password\n")

while True:
	if(len(password)<6):                                                                 
		print("Invalid password......\n")
		print("Enter more than 6 characters")
		break
	elif not re.search('[a-z]',password):
		print("Invalid password.......\n","<ENTER ATLEAST ONE LOWERCASE LETTER>")
		break
	elif not re.search('[A-Z]',password):
		print("Invalid password....\n","<ENTER ATLEAST ONE UPPERCASE LETTER>")
		break
	elif not re.search('[0-9]',password):
		print("Invalid password......\n","<ENTER ATLEAST ONE DECIMAL NUMBER>")
		break
	elif not re.search('[!@#$%^&*(),.?":{}|<>]',password):
		print("Invalid password.......\n","<ENTER ATLEAST ONE SYMBOL>")
		break
	else:
		print("IT IS VALID PASSWORD")
		break

print("PASSWORD ENTERED IS:",password)