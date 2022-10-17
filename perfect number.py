a=int(input())
i=1
sum=0
while i<a:
    if(a%i==0):
        sum=sum+i
        print(i)
    i=i+1
if a==sum:
    print(a,"perfect number")
else:
    print(a,"not perfect number")
    
    
    
a=int(input())
sum=0
i=1
for i in range(1,a):
    if (a)%i==0:
        sum=sum+i
        print(i)
        
if a==sum:
    print(a,"prefect number")
else:
    print(a,"not perfect number")