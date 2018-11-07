# Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete. 

my_dict = {'123456':'Adarsh', '4568745':'Dheeraj', '7895545':'Sajesh', '4254556':'Bantakal', '4632586':'Sunil', '9865874':'Chetas'}

print(my_dict)

my_dict['123457'] = 'Student' #to insert

print(my_dict)

print(my_dict.pop('123457'))  #to delete

print(my_dict)

