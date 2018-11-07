#Implement a program to create a list with two tuple of fruits and vegetables. Access fruits separately and vegetables separately. 

tuple1=('carrot','potato','tomato','beans')
print(tuple1)
tuple2=('mango','apple','banana','pineapple')
print(tuple2)
mylist=list(zip(tuple1,tuple2))
for i in range(len(mylist)):
     print(mylist[i])
