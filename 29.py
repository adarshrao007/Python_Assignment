n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
sum1=0
sum2=0
avg=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    sum3 = sum1  + sum2
    avg=(sum1+sum2)/n
print("Sum of all even numbers:",sum1)
print("Sum of all odd numbers:",sum2)
print("Sum of all numbers:",sum3)
print("average:",avg)