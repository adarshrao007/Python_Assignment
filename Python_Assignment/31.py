list=[1,2,3,4,4,3,2,1]
index = 0
while index < (len(list)/2):
	if list[index]==list[-1-index]:
		index+=1
		
	else:
		print("no") 
print("Yes")