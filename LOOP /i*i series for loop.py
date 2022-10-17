# a=int(input())
# for i in range(1,a):
#     print(i*i,end=" ")
    
a=int(input())
i=1
product=1
sum=0
for i in range(1,a):
    product=product*i
    sum=sum+product
    i=i+1
print(sum)

    
    