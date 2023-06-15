#Armstrong number

num=1000
sum=0
for i in range(1,num+1):
    j=i
    # print(j)
    length=int(len(str(i)))
    # print(i," ",length)
    while i!=0:
        res=i%10
        sum=sum+int(pow(res,length))
        i=int(i/10)
    # print(sum,end=" ")
    
    if j==sum:
        print(sum,end=" ")
    sum=0
print("\n--------------------------")
list1=[[1,2,3],[4,5,6],[7,8,9]]
a=list1[0]

print(a[0])

print("-----------------------------")