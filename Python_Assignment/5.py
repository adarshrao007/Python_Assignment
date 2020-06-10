#Implement a  program to check the elements in the list has word "SOIS"

list=['hi','hello','sois','mit','ncet']
str=input("enter the word to search")
if str in list:
	print("yes,sois is present in list:",list)
else:
	print("element not found")
